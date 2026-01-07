import base64
import json
import hmac
import hashlib
import argparse
from datetime import datetime, timezone

def b64url_decode(data):
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

def decode_part(part):
    return json.loads(b64url_decode(part).decode())

def verify_hs256(header, payload, signature, secret):
    signing_input = f"{header}.{payload}".encode()
    expected = hmac.new(
        secret.encode(),
        signing_input,
        hashlib.sha256
    ).digest()
    return hmac.compare_digest(expected, b64url_decode(signature))

def inspect_jwt(token, secret=None):
    header_b64, payload_b64, signature_b64 = token.split(".")

    header = decode_part(header_b64)
    payload = decode_part(payload_b64)

    print("\n[+] HEADER")
    print(json.dumps(header, indent=2))

    print("\n[+] PAYLOAD")
    print(json.dumps(payload, indent=2))

    print("\n[!] SECURITY ANALYSIS")

    if header.get("alg") == "none":
        print("❌ Insecure algorithm: NONE")

    if "exp" in payload:
        exp = datetime.fromtimestamp(payload["exp"], timezone.utc)
        if exp < datetime.now(timezone.utc):
            print("❌ Token expired")

    if secret and header.get("alg") == "HS256":
        valid = verify_hs256(header_b64, payload_b64, signature_b64, secret)
        print("✅ Signature valid" if valid else "❌ Invalid signature")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JWT Security Inspector")
    parser.add_argument("token", help="JWT token")
    parser.add_argument("--secret", help="HS256 secret", default=None)
    args = parser.parse_args()

    inspect_jwt(args.token, args.secret)
