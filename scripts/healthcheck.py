"""Healthcheck Docker : exit 0 si /<prefix>/health répond 200."""
import os
import sys
import urllib.request

prefix = os.environ.get("URL_PREFIX", "/__SLUG__").rstrip("/")
try:
    with urllib.request.urlopen(f"http://127.0.0.1:5000{prefix}/health", timeout=3) as r:
        sys.exit(0 if r.status == 200 else 1)
except Exception:
    sys.exit(1)
