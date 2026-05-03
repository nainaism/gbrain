#!/usr/bin/env python3
"""
gbrain-embed-external.py — Embed gbrain pages using external API (curl-style),
bypassing the PGLite WASM + OpenAI SDK incompatibility in bun.

Reads pages from PGLite via psycopg-compatible queries on the raw data files,
calls OpenRouter embedding API, and writes embeddings back.

Usage:
  source ~/.hermes/.env
  python3 gbrain-embed-external.py [--all] [--stale] [slug ...]
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Config
GBRAIN_HOME = Path.home() / ".gbrain"
CONFIG_PATH = GBRAIN_HOME / "config.json"
DB_PATH = GBRAIN_HOME / "brain.pglite"
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
BASE_URL = "https://openrouter.ai/api/v1/embeddings"
MODEL = "openai/text-embedding-3-large"
DIMENSIONS = 1536
MAX_CHARS = 8000


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def query_db(sql, params=None):
    """Query PGLite via bun (avoids Python psycopg dependency)."""
    cmd = ["bun", "-e", f"""
import {{ PGlite }} from '@electric-sql/pglite';
const db = await PGlite.create('{DB_PATH}');
const result = await db.query(`{sql}`, {json.dumps(params) if params else '[]'});
console.log(JSON.stringify(result.rows));
await db.close();
"""]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=os.path.expanduser("~/gbrain"))
    if result.returncode != 0:
        print(f"DB error: {result.stderr[:200]}", file=sys.stderr)
        return []
    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return []


def exec_db(sql, params=None):
    """Execute SQL via bun."""
    cmd = ["bun", "-e", f"""
import {{ PGlite }} from '@electric-sql/pglite';
const db = await PGlite.create('{DB_PATH}');
await db.query(`{sql}`, {json.dumps(params) if params else '[]'});
console.log('OK');
await db.close();
"""]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=os.path.expanduser("~/gbrain"))
    if result.returncode != 0:
        print(f"DB exec error: {result.stderr[:200]}", file=sys.stderr)
        return False
    return "OK" in result.stdout


def get_embedding(text):
    """Call OpenRouter embedding API via curl."""
    truncated = text[:MAX_CHARS]
    payload = json.dumps({
        "model": MODEL,
        "input": truncated,
        "dimensions": DIMENSIONS,
    })
    cmd = [
        "curl", "-s", BASE_URL,
        "-H", f"Authorization: Bearer {OPENROUTER_KEY}",
        "-H", "Content-Type: application/json",
        "-d", payload,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    try:
        data = json.loads(result.stdout)
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["embedding"]
        else:
            print(f"  API error: {result.stdout[:200]}", file=sys.stderr)
            return None
    except json.JSONDecodeError:
        print(f"  JSON decode error: {result.stdout[:200]}", file=sys.stderr)
        return None


def embed_page(slug):
    """Embed a single page."""
    rows = query_db(
        "SELECT slug, compiled_truth, timeline FROM pages WHERE slug = $1",
        [slug]
    )
    if not rows:
        print(f"  SKIP (not found): {slug}")
        return False

    page = rows[0]
    text = "\n\n".join(filter(None, [page.get("compiled_truth", ""), page.get("timeline", "")]))
    if not text.strip():
        print(f"  SKIP (empty): {slug}")
        return False

    embedding = get_embedding(text)
    if not embedding:
        print(f"  FAIL: {slug}")
        return False

    # Check if chunk already exists
    existing = query_db(
        "SELECT chunk_index FROM content_chunks WHERE slug = $1 AND chunk_index = 0",
        [slug]
    )

    emb_str = "[" + ",".join(str(x) for x in embedding) + "]"
    token_count = len(text) // 4

    if existing:
        # Update existing chunk
        ok = exec_db(
            """UPDATE content_chunks SET embedding = $1::vector, token_count = $2, embedded_at = NOW()
               WHERE slug = $3 AND chunk_index = 0""",
            [emb_str, token_count, slug]
        )
    else:
        # Insert new chunk
        ok = exec_db(
            """INSERT INTO content_chunks (slug, chunk_index, chunk_text, chunk_source, embedding, token_count, embedded_at)
               VALUES ($1, 0, $2, 'compiled_truth', $3::vector, $4, NOW())""",
            [slug, text[:MAX_CHARS], emb_str, token_count]
        )

    if ok:
        print(f"  OK: {slug} ({len(embedding)}d)")
    return ok


def main():
    if not OPENROUTER_KEY:
        print("Error: OPENROUTER_API_KEY not set. Run: source ~/.hermes/.env", file=sys.stderr)
        sys.exit(1)

    args = sys.argv[1:]
    if not args or "--all" in args or "--stale" in args:
        # Get all non-readme pages
        rows = query_db(
            "SELECT slug FROM pages WHERE slug NOT LIKE '%readme' AND slug NOT LIKE '%resolver%' ORDER BY slug"
        )
        slugs = [r["slug"] for r in rows]
    else:
        slugs = [a for a in args if not a.startswith("--")]

    print(f"Embedding {len(slugs)} pages...")
    success = 0
    for slug in slugs:
        if embed_page(slug):
            success += 1
    print(f"\nDone: {success}/{len(slugs)} embedded")


if __name__ == "__main__":
    main()
