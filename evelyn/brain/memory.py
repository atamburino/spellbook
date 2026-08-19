"""Local-first memory for Evelyn.

Two kinds of memory, both in one SQLite file that lives in data/ and never
leaves your machine:

- facts: durable, key -> value knowledge ("wife's birthday" -> "June 3rd").
  Overwriting a key updates it, so facts stay current instead of piling up.
- conversation_log: a timestamped transcript of every turn, used to answer
  "what did we just talk about?" and similar recency questions.

This is intentionally simple (no embeddings, no vector DB) so the MVP has
zero extra infra to run. The recall() method does recency + naive keyword
matching. Swapping in a vector store (e.g. sqlite-vec) later is a drop-in
replacement for recall() — nothing else in the codebase needs to change,
since agent.py and the tools only ever go through this module.
"""

from __future__ import annotations

import sqlite3
from contextlib import closing
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "evelyn.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS facts (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS conversation_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""


@dataclass
class Turn:
    role: str
    content: str
    created_at: str


class Memory:
    """Owns the SQLite connection and every read/write to it."""

    def __init__(self, db_path: Path | str = DEFAULT_DB_PATH):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with closing(self._connect()) as conn:
            conn.executescript(SCHEMA)
            conn.commit()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    # -- facts ---------------------------------------------------------

    def remember_fact(self, key: str, value: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with closing(self._connect()) as conn:
            conn.execute(
                """
                INSERT INTO facts (key, value, updated_at) VALUES (?, ?, ?)
                ON CONFLICT(key) DO UPDATE SET value = excluded.value,
                                                updated_at = excluded.updated_at
                """,
                (key.strip().lower(), value, now),
            )
            conn.commit()

    def get_fact(self, key: str) -> str | None:
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT value FROM facts WHERE key = ?", (key.strip().lower(),)
            ).fetchone()
        return row[0] if row else None

    def all_facts(self) -> dict[str, str]:
        with closing(self._connect()) as conn:
            rows = conn.execute("SELECT key, value FROM facts ORDER BY key").fetchall()
        return dict(rows)

    # -- conversation log ------------------------------------------------

    def log_turn(self, role: str, content: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with closing(self._connect()) as conn:
            conn.execute(
                "INSERT INTO conversation_log (role, content, created_at) VALUES (?, ?, ?)",
                (role, content, now),
            )
            conn.commit()

    def recent_turns(self, limit: int = 20) -> list[Turn]:
        with closing(self._connect()) as conn:
            rows = conn.execute(
                "SELECT role, content, created_at FROM conversation_log "
                "ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [Turn(*row) for row in reversed(rows)]

    def recall(self, query: str, limit: int = 10) -> list[Turn]:
        """Naive keyword search over the log, most recent match first.

        Good enough for "what did we just talk about X" at MVP scale. Once
        the log gets large or the questions get fuzzier, replace this body
        with a real embedding search — callers don't need to change.
        """
        words = [w for w in query.lower().split() if len(w) > 2]
        if not words:
            return self.recent_turns(limit)
        like_clauses = " OR ".join(["LOWER(content) LIKE ?"] * len(words))
        params = [f"%{w}%" for w in words]
        with closing(self._connect()) as conn:
            rows = conn.execute(
                f"SELECT role, content, created_at FROM conversation_log "
                f"WHERE {like_clauses} ORDER BY id DESC LIMIT ?",
                (*params, limit),
            ).fetchall()
        return [Turn(*row) for row in reversed(rows)]
