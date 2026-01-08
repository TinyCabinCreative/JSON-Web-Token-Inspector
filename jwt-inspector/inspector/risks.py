from datetime import datetime, timezone
from typing import List
from .models import DecodedJWT, RiskFinding


def check_none_algorithm(jwt: DecodedJWT) -> List[RiskFinding]:
    findings = []
    if jwt.header.get("alg", "").lower() == "none":
        findings.append(RiskFinding(
            severity="HIGH",
            message="JWT uses 'alg=none' which disables signature verification"
        ))
    return findings


def check_expiration(jwt: DecodedJWT) -> List[RiskFinding]:
    findings = []
    exp = jwt.payload.get("exp")

    if exp is None:
        findings.append(RiskFinding(
            severity="MEDIUM",
            message="Token has no expiration (exp) claim"
        ))
        return findings

    try:
        exp_time = datetime.fromtimestamp(exp, timezone.utc)
        if exp_time < datetime.now(timezone.utc):
            findings.append(RiskFinding(
                severity="HIGH",
                message="Token is expired"
            ))
    except Exception:
        findings.append(RiskFinding(
            severity="LOW",
            message="Invalid exp claim format"
        ))

    return findings


def check_missing_claims(jwt: DecodedJWT) -> List[RiskFinding]:
    findings = []
    for claim in ("iss", "aud", "sub"):
        if claim not in jwt.payload:
            findings.append(RiskFinding(
                severity="LOW",
                message=f"Missing standard claim: {claim}"
            ))
    return findings


def run_all_checks(jwt: DecodedJWT) -> List[RiskFinding]:
    findings = []
    findings.extend(check_none_algorithm(jwt))
    findings.extend(check_expiration(jwt))
    findings.extend(check_missing_claims(jwt))
    return findings
