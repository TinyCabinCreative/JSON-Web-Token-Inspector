import json
from typing import List
from .models import RiskFinding


def pretty_print(title: str, data: dict):
    print(f"\n[+] {title}")
    print(json.dumps(data, indent=2))


def print_findings(findings: List[RiskFinding]):
    if not findings:
        print("\n✅ No security issues detected")
        return

    print("\n[!] SECURITY FINDINGS")
    for finding in findings:
        print(f"[{finding.severity}] {finding.message}")
