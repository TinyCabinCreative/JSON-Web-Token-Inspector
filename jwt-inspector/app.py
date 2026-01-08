from flask import Flask, render_template, request
from inspector.decoder import decode_jwt
from inspector.risks import run_all_checks
from inspector.verifier import verify_hs256
from inspector.models import RiskFinding

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None

    if request.method == "POST":
        token = request.form.get("token")
        secret = request.form.get("secret")

        try:
            jwt = decode_jwt(token)
            findings = run_all_checks(jwt)

            if secret and jwt.header.get("alg") == "HS256":
                valid = verify_hs256(
                    jwt.header_b64,
                    jwt.payload_b64,
                    jwt.signature_b64,
                    secret
                )
                if not valid:
                    findings.append(
                        RiskFinding("HIGH", "Invalid HS256 signature")
                    )

            results = {
                "header": jwt.header,
                "payload": jwt.payload,
                "findings": findings
            }

        except Exception as e:
            error = str(e)

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)
