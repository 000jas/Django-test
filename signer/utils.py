import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# Load keys from environment variables
PRIVATE_KEY_PEM = os.environ.get("PRIVATE_KEY_PEM")
PUBLIC_KEY_PEM = os.environ.get("PUBLIC_KEY_PEM")

private_key = serialization.load_pem_private_key(
    PRIVATE_KEY_PEM.encode(), password=None
)

public_key = serialization.load_pem_public_key(
    PUBLIC_KEY_PEM.encode()
)

def sign_message(message: bytes) -> bytes:
    return private_key.sign(message)

def verify_signature(message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(signature, message)
        return True
    except:
        return False
