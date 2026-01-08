#  JWT Inspector

JWT Inspector is a lightweight security analysis tool for inspecting JSON Web Tokens (JWTs) and identifying common authentication misconfigurations.

It is designed as:
- a reusable Python security library
- a local web application (Flask)
- a containerized, reproducible security tool (Docker)

It is designed to:
To Stakeholders:
“It’s a safety check that helps teams catch authentication mistakes before they become security incidents."

To Nerds: 
- It reduces the risk of account takeovers, data leaks, and compliance issues — without slowing down developers.
- It runs locally, doesn’t send data anywhere, and is isolated so sensitive information isn’t exposed.
- By separating the analysis logic from the interface and containerizing it, I made something that could realistically be used by a team.
- JWTs fail more often due to misconfiguration, not cryptographic failure.

This tool looks for:
alg=none (signature bypass)
expired tokens
missing standard claims
invalid HS256 signatures

---

##  Why JWT Inspector Exists

JWT misconfigurations are a frequent cause of:
- authentication bypass
- privilege escalation
- broken session handling

JWT Inspector helps developers and security professionals:
- understand JWT internals
- identify insecure token configurations
- safely analyze tokens in an isolated environment

---

##  Features

- Decode JWT headers and payloads
- Detect insecure algorithms (`alg=none`)
- Identify expired or non-expiring tokens
- Highlight missing standard claims (`iss`, `aud`, `sub`)
- Verify HS256 signatures (optional secret)
- Clean web UI for interactive analysis
- Fully containerized for safe execution

---

## Architecture Overview


jwt-inspector/
├── README.md
├── inspector/
│   ├── __init__.py
│   ├── jwt_inspector.py
│   ├── risks.py
│   └── utils.py
├── samples/
│   ├── weak_hs256.jwt
│   ├── expired.jwt
│   └── none_alg.jwt
├── tools/
│   ├── java-token-generator/
│   │   └── TokenGenerator.java
│   └── cpp-token-generator/
│       └── token_generator.cpp
└── requirements.txt
