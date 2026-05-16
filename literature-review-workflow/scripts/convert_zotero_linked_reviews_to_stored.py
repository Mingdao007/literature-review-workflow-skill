#!/usr/bin/env python3
"""Convert Zotero review linked PDFs into stored attachments.

This script handles the specific Zotero workflow where final review PDFs were
previously inserted as standalone linked attachments pointing at
~/Zotero/Reviews. Such absolute paths do not open on another machine. The safe
repair is to keep the linked item as legacy evidence and create a fresh stored
attachment item from birth, because Zotero does not allow changing an existing
attachment's linkMode after sync.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import sqlite3
import time
from pathlib import Path


KEY_ALPHABET = "23456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
LEGACY_SUFFIX = " (legacy linked path)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db",
        default=str(Path.home() / "Zotero" / "zotero.sqlite"),
        help="Path to zotero.sqlite",
    )
    parser.add_argument(
        "--reviews-prefix",
        default=str(Path.home() / "Zotero" / "Reviews") + "/",
        help="Absolute linked-file prefix to convert",
    )
    parser.add_argument(
        "--collection-id",
        type=int,
        action="append",
        help="Limit to one or more Zotero collection IDs. Omit to convert all matching collections.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Mutate zotero.sqlite. Without this flag the script only reports candidates.",
    )
    return parser.parse_args()


def connect(db_path: Path, *, read_only: bool) -> sqlite3.Connection:
    if read_only:
        uri = f"file:{db_path}?mode=ro&immutable=1"
        conn = sqlite3.connect(uri, uri=True, isolation_level=None)
    else:
        conn = sqlite3.connect(str(db_path), isolation_level=None)
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=1000")
    return conn


def get_value_id(cur: sqlite3.Cursor, value: str) -> int:
    cur.execute("INSERT OR IGNORE INTO itemDataValues(value) VALUES (?)", (value,))
    row = cur.execute("SELECT valueID FROM itemDataValues WHERE value=?", (value,)).fetchone()
    if not row:
        raise RuntimeError(f"Could not resolve valueID for {value!r}")
    return int(row[0])


def new_item_key(cur: sqlite3.Cursor, storage_root: Path) -> str:
    existing = {row[0] for row in cur.execute("SELECT key FROM items")}
    while True:
        key = "".join(random.choice(KEY_ALPHABET) for _ in range(8))
        if key not in existing and not (storage_root / key).exists():
            return key


def load_candidates(cur: sqlite3.Cursor, reviews_prefix: str, collection_ids: list[int] | None) -> list[dict]:
    params: list[object] = [reviews_prefix + "%", LEGACY_SUFFIX]
    collection_filter = ""
    if collection_ids:
        placeholders = ",".join("?" for _ in collection_ids)
        collection_filter = f" AND ci.collectionID IN ({placeholders})"
        params.extend(collection_ids)

    rows = cur.execute(
        f"""
        SELECT
            i.itemID,
            i.key,
            i.libraryID,
            COALESCE(iv.value, '') AS title,
            ia.path,
            group_concat(ci.collectionID),
            group_concat(ci.orderIndex)
        FROM items i
        JOIN itemAttachments ia ON ia.itemID=i.itemID
        JOIN collectionItems ci ON ci.itemID=i.itemID
        LEFT JOIN itemData id
            ON id.itemID=i.itemID
            AND id.fieldID=(SELECT fieldID FROM fieldsCombined WHERE fieldName='title')
        LEFT JOIN itemDataValues iv ON iv.valueID=id.valueID
        WHERE ia.parentItemID IS NULL
          AND ia.linkMode=2
          AND ia.contentType='application/pdf'
          AND ia.path LIKE ?
          AND COALESCE(iv.value, '') NOT LIKE '%' || ?
          {collection_filter}
        GROUP BY i.itemID
        ORDER BY i.itemID
        """,
        params,
    ).fetchall()

    candidates = []
    for row in rows:
        collection_ids_raw = str(row[5]).split(",") if row[5] else []
        order_indexes_raw = str(row[6]).split(",") if row[6] else []
        candidates.append(
            {
                "itemID": int(row[0]),
                "key": row[1],
                "libraryID": int(row[2]),
                "title": row[3],
                "path": row[4],
                "collections": [
                    (int(cid), int(order_indexes_raw[idx]))
                    for idx, cid in enumerate(collection_ids_raw)
                ],
            }
        )
    return candidates


def convert_one(
    cur: sqlite3.Cursor,
    storage_root: Path,
    candidate: dict,
    now_utc: str,
    title_field_id: int,
) -> dict:
    source = Path(candidate["path"])
    if not source.exists():
        return {"itemID": candidate["itemID"], "title": candidate["title"], "status": "missing_file", "path": str(source)}

    stored_key = new_item_key(cur, storage_root)
    stored_dir = storage_root / stored_key
    stored_dir.mkdir(parents=True, exist_ok=False)
    stored_path = stored_dir / source.name

    try:
        shutil.copy2(source, stored_path)
        stat = stored_path.stat()
        storage_mtime_ms = int(stat.st_mtime * 1000)
        storage_mtime_sec = int(stat.st_mtime)
        storage_hash = hashlib.md5(stored_path.read_bytes()).hexdigest()

        old_title = candidate["title"]
        legacy_title = old_title + LEGACY_SUFFIX
        old_title_value_id = get_value_id(cur, legacy_title)
        new_title_value_id = get_value_id(cur, old_title)

        cur.execute(
            """
            INSERT INTO itemData(itemID, fieldID, valueID) VALUES (?, ?, ?)
            ON CONFLICT(itemID, fieldID) DO UPDATE SET valueID=excluded.valueID
            """,
            (candidate["itemID"], title_field_id, old_title_value_id),
        )
        cur.execute("DELETE FROM collectionItems WHERE itemID=?", (candidate["itemID"],))
        cur.execute(
            """
            UPDATE items
            SET synced=0, dateModified=?, clientDateModified=?
            WHERE itemID=?
            """,
            (now_utc, now_utc, candidate["itemID"]),
        )

        cur.execute(
            """
            INSERT INTO items(itemTypeID, dateAdded, dateModified, clientDateModified, libraryID, key, version, synced)
            VALUES (3, ?, ?, ?, ?, ?, 0, 0)
            """,
            (now_utc, now_utc, now_utc, candidate["libraryID"], stored_key),
        )
        new_item_id = int(cur.lastrowid)
        cur.execute(
            """
            INSERT INTO itemAttachments(
                itemID, parentItemID, linkMode, contentType, charsetID, path,
                syncState, storageModTime, storageHash, lastProcessedModificationTime, lastRead
            ) VALUES (?, NULL, 0, 'application/pdf', NULL, ?, 0, ?, ?, ?, NULL)
            """,
            (new_item_id, f"storage:{source.name}", storage_mtime_ms, storage_hash, storage_mtime_sec),
        )
        cur.execute(
            "INSERT INTO itemData(itemID, fieldID, valueID) VALUES (?, ?, ?)",
            (new_item_id, title_field_id, new_title_value_id),
        )
        for collection_id, order_index in candidate["collections"]:
            cur.execute(
                "INSERT INTO collectionItems(collectionID, itemID, orderIndex) VALUES (?, ?, ?)",
                (collection_id, new_item_id, order_index),
            )

        return {
            "oldItemID": candidate["itemID"],
            "oldKey": candidate["key"],
            "newItemID": new_item_id,
            "newKey": stored_key,
            "title": old_title,
            "storedPath": str(stored_path),
            "storageHash": storage_hash,
            "collections": [cid for cid, _ in candidate["collections"]],
            "status": "converted",
        }
    except Exception:
        shutil.rmtree(stored_dir, ignore_errors=True)
        raise


def main() -> int:
    args = parse_args()
    db_path = Path(args.db).expanduser()
    storage_root = db_path.parent / "storage"

    conn = connect(db_path, read_only=not args.apply)
    cur = conn.cursor()
    candidates = load_candidates(cur, args.reviews_prefix, args.collection_id)

    if not args.apply:
        print(json.dumps({"mode": "dry-run", "candidateCount": len(candidates), "candidates": candidates}, ensure_ascii=False, indent=2))
        conn.close()
        return 0

    backup = db_path.with_name(db_path.name + f".backup_linked_reviews_to_stored_{time.strftime('%Y%m%d_%H%M%S')}")
    shutil.copy2(db_path, backup)

    title_field_id = int(cur.execute("SELECT fieldID FROM fieldsCombined WHERE fieldName='title'").fetchone()[0])
    now_utc = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    results: list[dict] = []
    try:
        cur.execute("BEGIN IMMEDIATE")
        for candidate in candidates:
            result = convert_one(cur, storage_root, candidate, now_utc, title_field_id)
            results.append(result)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print(json.dumps({"mode": "apply", "backup": str(backup), "convertedCount": sum(r["status"] == "converted" for r in results), "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
