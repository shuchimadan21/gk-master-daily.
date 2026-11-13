#!/usr/bin/env python3
"""Rebuild editions/index.json from the edition files (newest first)."""
import json, os, re
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "editions")
ids = sorted((f[:-5] for f in os.listdir(here) if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.json", f)), reverse=True)
with open(os.path.join(here, "index.json"), "w") as fh:
    json.dump({"editions": ids}, fh, indent=1)
print(len(ids), "editions; latest", ids[0] if ids else None)
