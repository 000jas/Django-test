import os
from django.core.management.base import BaseCommand
from django.conf import settings
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

class Command(BaseCommand):
    help = 'Generate Ed25519 keypair and write to disk (default paths from settings)'

    def add_arguments(self, parser):
        parser.add_argument('--priv', type=str, help='Path to private key file', default='keys/signer_key.pem')
        parser.add_argument('--pub', type=str, help='Path to public key file', default='keys/signer_key.pub')

    def handle(self, *args, **options):
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()

        priv_path = options['priv']
        pub_path = options['pub']

        os.makedirs(os.path.dirname(priv_path), exist_ok=True)

        with open(priv_path, 'wb') as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

        with open(pub_path, 'wb') as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

        self.stdout.write(self.style.SUCCESS(f"Keys written: {priv_path}, {pub_path}"))
