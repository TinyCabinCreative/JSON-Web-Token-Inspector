# JWT Inspector 🔐

A lightweight security tool that analyzes JSON Web Tokens (JWTs) for common vulnerabilities and misconfigurations.

## Features
- Decode JWT headers and payloads
- Detect insecure algorithms (`alg=none`)
- Identify expired tokens
- Verify HS256 signatures
- Highlight risky configurations

## Usage
```bash
python jwt_inspector.py <token> --secret <optional-secret>

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
