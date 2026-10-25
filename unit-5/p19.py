
# Practical 19: Hashed Password Verification

import hashlib
import hmac
import getpass

# 1. Accept a sample password
password = getpass.getpass("Create a password: ")

# 2. Generate SHA-256 digest
password_digest = hashlib.sha256(
    password.encode("utf-8")
).hexdigest()

# 3. Store the digest instead of the original password
with open("password_hash.txt", "w") as file:
    file.write(password_digest)

print("Password digest stored successfully.")

# 4. Read the stored digest
with open("password_hash.txt", "r") as file:
    stored_digest = file.read().strip()

# 5. Accept password for verification
entered_password = getpass.getpass("Enter password to verify: ")

# 6. Generate digest of entered password
entered_digest = hashlib.sha256(
    entered_password.encode("utf-8")
).hexdigest()

# 7. Verify the password
if hmac.compare_digest(entered_digest, stored_digest):
    print("Password verification successful!")
else:
    print("Password verification failed!")
