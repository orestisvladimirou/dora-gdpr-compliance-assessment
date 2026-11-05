#!/usr/bin/env python3
"""Check the current fictional DORA/GDPR portfolio's exact file inventory and hashes."""
import hashlib
import json
from pathlib import Path
from validate_project import ROOT

SKIP={".git","__pycache__",".pytest_cache"}

def inventory():
    result={}
    for p in ROOT.rglob("*"):
        if not p.is_file() or any(x in SKIP for x in p.relative_to(ROOT).parts) or p.suffix in (".pyc",".pyo"):
            continue
        if p.name=="SOURCE_MANIFEST.json":
            continue
        b=p.read_bytes()
        result[p.relative_to(ROOT).as_posix()]={"sha256":hashlib.sha256(b).hexdigest(),"size":len(b)}
    return result

def validate_manifest():
    content=json.loads((ROOT/"SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    assert content["version"]=="0.4", "Current manifest must be version 0.4"
    listed={r["path"]:{"sha256":r["sha256"],"size":r["size"]} for r in content["files"]}
    actual=inventory()
    assert listed==actual, "Source inventory differs from checked v0.4 manifest"
    print(f"PASS manifest: {len(actual)} portfolio source and workbook files match verified hashes")
    return True

if __name__=="__main__":
    validate_manifest()
