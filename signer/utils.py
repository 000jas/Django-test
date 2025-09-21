from django.conf import settings
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from pathlib import Path
import base64




def _read_file(path):
	p = Path(path)
	if not p.exists():
		raise FileNotFoundError(f"Key file not found: {p}")
	return p.read_bytes()




def load_private_key(path=None):
	path = path or settings.SIGNER_PRIV_KEY
	data = _read_file(path)
	return load_pem_private_key(data, password=None)




def load_public_key(path=None):
	path = path or settings.SIGNER_PUB_KEY
	data = _read_file(path)
	return load_pem_public_key(data)




def sign_message(message: bytes) -> bytes:
	"""Return raw signature bytes for `message`."""
	priv = load_private_key()
	return priv.sign(message)




def sign_message_b64(message: bytes) -> str:
	return base64.b64encode(sign_message(message)).decode('ascii')




def verify_signature(message: bytes, signature: bytes, public_key=None) -> bool:
	if public_key is None:
		public_key = load_public_key()
	try:
		public_key.verify(signature, message)
		return True
	except Exception:
		return False