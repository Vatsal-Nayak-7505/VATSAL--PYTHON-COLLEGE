
# Practical 21: Secure File Access System

import os
import json
import getpass

from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError
)
from cryptography.fernet import Fernet, InvalidToken

USERS_FILE = "users.json"
KEY_FILE = "secret.key"
DATA_FILE = "protected.bin"

hasher = PasswordHasher()


# 1. Register a user on the first run
if not os.path.exists(USERS_FILE):
    print("First-time setup: Create an account.")

    username = input("Create username: ").strip()
    password = getpass.getpass("Create password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        raise SystemExit

    password_hash = hasher.hash(password)

    with open(USERS_FILE, "w") as file:
        json.dump({username: password_hash}, file)

    print("Account created. Password hash stored.")


# 2. Prepare the encryption key safely
if not os.path.exists(KEY_FILE):
    if os.path.exists(DATA_FILE):
        print("Error: Encryption key is missing.")
        print("Cannot safely decrypt the existing file.")
        raise SystemExit

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

# Load the existing key
try:
    with open(KEY_FILE, "rb") as file:
        key = file.read()

    cipher = Fernet(key)

except (OSError, ValueError):
    print("Error: Encryption key is missing or invalid.")
    raise SystemExit


# 3. Create encrypted sample content if needed
if not os.path.exists(DATA_FILE):
    try:
        sample = b"Confidential student information.\n"
        encrypted = cipher.encrypt(sample)

        with open(DATA_FILE, "wb") as file:
            file.write(encrypted)

        print("Encrypted file initialized.")

    except OSError:
        print("Error: Could not create the protected file.")
        raise SystemExit


# 4. Verify login credentials
try:
    with open(USERS_FILE, "r") as file:
        users = json.load(file)

except (OSError, json.JSONDecodeError):
    print("Error: User account file is missing or invalid.")
    raise SystemExit

username = input("\nUsername: ").strip()
password = getpass.getpass("Password: ")

stored_hash = users.get(username)
authenticated = False

if stored_hash:
    try:
        authenticated = hasher.verify(stored_hash, password)
    except (
        VerifyMismatchError,
        VerificationError,
        InvalidHashError
    ):
        authenticated = False

if not authenticated:
    print("Login failed. Access denied.")
    raise SystemExit

print("\nLogin successful. Access granted.")


# 5. Read protected content or append data
try:
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()

    # Decrypt only after authentication
    plaintext = cipher.decrypt(encrypted_data)

    print("\n1. Read protected file")
    print("2. Append data")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        print("\nProtected File Contents:")
        print(plaintext.decode("utf-8"))

    elif choice == "2":
        new_record = input("Enter data to append: ")

        updated_content = (
            plaintext.rstrip(b"\n")
            + b"\n"
            + new_record.encode("utf-8")
            + b"\n"
        )

        # Encrypt the updated content
        updated_encrypted = cipher.encrypt(updated_content)

        with open(DATA_FILE, "wb") as file:
            file.write(updated_encrypted)

        print("Data appended and encrypted successfully.")

    else:
        print("Invalid menu option.")

except FileNotFoundError:
    print("Error: Protected file or key file not found.")

except InvalidToken:
    print("Error: Decryption failed. Key or data is invalid.")

except (OSError, UnicodeError, ValueError):
    print("Error: Unable to process the protected file.")
    