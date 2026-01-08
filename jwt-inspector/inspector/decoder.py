import base64
import json
from typing import Dict
from .models import JWTParts, DecodedJWT


class JWTDecodeError(Exception):
    pass


def _b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def split_token(token: str) -> JWTParts:
    parts = token.split(".")
    if len(parts) != 3:
        raise JWTDecodeError("Invalid JWT format")

    return JWTParts(*parts)


def decode_part(part: str) -> Dict:
    try:
        decoded = _b64url_decode(part)
        return json.loads(decoded.decode("utf-8"))
    except Exception as e:
        raise JWTDecodeError(f"Failed to decode JWT part: {e}")


def decode_jwt(token: str) -> DecodedJWT:
    parts = split_token(token)

    header = decode_part(parts.header_b64)
    payload = decode_part(parts.payload_b64)

    return DecodedJWT(
        header=header,
        payload=payload,
        signature_b64=parts.signature_b64
    )
