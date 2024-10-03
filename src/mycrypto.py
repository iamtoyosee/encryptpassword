from cryptography.fernet import Fernet
import os

# Generate and store encryption key (only if it doesn't already exist)
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        generate_key()
        return load_key()

# Encrypt the password
def encrypt_password(password):
    key = load_key()  # Load the key (don't generate a new one each time)
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())  # Encrypt password
    return encrypted_password.decode()  # Return as string for storage

# Decrypt the password
def decrypt_password(encrypted_password):
    key = load_key()  # Load the key
    f = Fernet(key)
    try:
        decrypted_password = f.decrypt(encrypted_password.encode())  # Decrypt password
        return decrypted_password.decode()  # Return as plaintext
    except Exception as e:
        return None  # Handle decryption failure
