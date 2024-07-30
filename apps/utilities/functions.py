"""Functions for Utilities App."""

from django.conf import settings
from cryptography.fernet import Fernet, InvalidToken


try:
    f = Fernet(settings.ENCRYPT_KEY)
except ValueError:
    raise ValueError("The encryption key is not valid.")


def encrypt_field(field):
    """Encrypts a given field using the Fernet symmetric encryption."""
    try:
        field_bytes = field.encode("utf-8")
        encrypted_field = f.encrypt(field_bytes)
        return encrypted_field.decode("utf-8")
    except Exception as e:
        raise Exception(f"Error encrypting the field: {str(e)}")


def decrypt_field(encrypted_field):
    """Decrypts an encrypted field using the Fernet symmetric encryption."""
    try:
        encrypted_bytes = encrypted_field.encode("utf-8")
        field_bytes = f.decrypt(encrypted_bytes)
        return field_bytes.decode("utf-8")
    except InvalidToken:
        raise ValueError(
            "The encrypted field is not valid or the encryption key is incorrect."
        )
    except Exception as e:
        raise Exception(f"Error decrypting the field: {str(e)}")
