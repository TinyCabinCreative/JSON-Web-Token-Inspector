from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class JWTParts:
    header_b64: str
    payload_b64: str
    signature_b64: str


@dataclass
class DecodedJWT:
    header: Dict[str, Any]
    payload: Dict[str, Any]
    signature_b64: str


@dataclass
class RiskFinding:
    severity: str   # LOW / MEDIUM / HIGH
    message: str
