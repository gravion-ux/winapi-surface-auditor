"""CLI for winapi-surface-auditor."""
import argparse
import json
import sys
from pathlib import Path

from .scanner import scan_text, summarise


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Audit C/C++ source for risky Windows API usage.")
    p.add_argument("paths", nargs="+", help="Source files to scan")
    p.add_argument("--format", choices=["text", "json"], default="text")
    args = p.parse_args(argv)
    all_findings = []
    for raw in args.paths:
        path = Path(raw)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for f in scan_text(text):
            all_findings.append({"file": str(path), "api": f.api, "category": f.category,
                                 "severity": f.severity, "line": f.line, "snippet": f.snippet,
                                 "why": f.why, "safer": f.safer})
    if args.format == "json":
        print(json.dumps({"findings": all_findings}, indent=2))
    else:
        for f in all_findings:
            print(f"{f['file']}:{f['line']} [{f['severity']}] {f['api']} — {f['why']}")
            print(f"    safer: {f['safer']}")
        print(summarise([]) if not all_findings else f"total findings: {len(all_findings)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
