#!/usr/bin/env python3
"""Rebuild current source manifest only after intentionally controlled repository updates."""
import json
from validate_project import ROOT
from validate_manifest import inventory

def main():
    all_files=inventory()
    doc={
        "project":"DORA-GDPR-Compliance-Assessment",
        "version":"0.4",
        "fictional_case":True,
        "purpose":"Independent simulated compliance-assessment portfolio; no regulator reports",
        "files":[{"path":name,"sha256":record["sha256"],"size":record["size"]}
                 for name,record in sorted(all_files.items())]
    }
    (ROOT/"SOURCE_MANIFEST.json").write_text(
        json.dumps(doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Generated current v0.4 manifest: {len(all_files)} source files")

if __name__=="__main__":
    main()
