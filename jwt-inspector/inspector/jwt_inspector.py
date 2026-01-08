import argparse
from inspector.decoder import decode_jwt
from inspector.verifier import verify_hs256
from inspector.risks import run_all_checks
from inspector.utils import pretty_print, print_findings


def main():
    parser = argparse.ArgumentParser(description="JWT Security Inspector")
    parser.add_argument("token", help="JWT token to inspect")
    parser.add_argument("--secret", help="HS256 secret (optional)", default=None)

    args = parser.parse_args()

    jwt = decode_jwt(args.token)

    pretty_print("HEADER", jwt.header)
    pretty_print("PAYLOAD", jwt.payload)

    findings = run_all_checks(jwt)

    if args.secret and jwt.header.get("alg") == "HS256":
        valid = verify_hs256(
            jwt.header_b64 if hasattr(jwt, "header_b64") else "",
            jwt.payload_b64 if hasattr(jwt, "payload_b64") else "",
            jwt.signature_b64,
            args.secret
        )
        if not valid:
            findings.append(
                RiskFinding("HIGH", "Invalid HS256 signature")
            )

    print_findings(findings)


if __name__ == "__main__":
    main()
