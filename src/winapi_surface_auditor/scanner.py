"""Scan C/C++ source text for risky Windows API usage."""
import re
from dataclasses import dataclass

from .rules import RULE_BY_API


@dataclass
class Finding:
    api: str
    category: str
    severity: str
    line: int
    snippet: str
    why: str
    safer: str

def scan_text(text: str) -> list[Finding]:
    findings = []
    lines = text.splitlines()
    for api, rule in RULE_BY_API.items():
        pattern = re.compile(r"\b" + re.escape(api) + r"\s*\(")
        for i, line in enumerate(lines, 1):
            if pattern.search(line):
                findings.append(Finding(api, rule.category, rule.severity, i,
                                        line.strip()[:120], rule.why, rule.safer))
    findings.sort(key=lambda f: (f.line, f.api))
    return findings

def summarise(findings: list[Finding]) -> dict:
    counts = {"high": 0, "medium": 0, "low": 0}
    for f in findings:
        counts[f.severity] += 1
    return {"total": len(findings), "by_severity": counts,
            "apis": sorted({f.api for f in findings})}
