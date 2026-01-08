import hmac
import hashlib
from typing import Optional


class VerificationError(Exception):
    pass


def verify_hs256(
    header_b64: str,
    payload_b64: str,
    signature_b64: str,
    secret: str
) -> bool:
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")

    expected = hmac.new(
        secret.encode("utf-8"),
        signing_input,
        hashlib.sha256
    ).digest()

    try:
        from base64 import urlsafe_b64decode
        padding = "=" * (-len(signature_b64) % 4)
        actual = urlsafe_b64decode(signature_b64 + padding)
    except Exception as e:
        raise VerificationError(f"Invalid signature encoding: {e}")

    return hmac.compare_digest(expected, actual)
