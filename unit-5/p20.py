
# Practical 20: Basic File Encryption and Decryption

from cryptography.fernet import Fernet, InvalidToken

# 1. Create a file with confidential text
with open("confidential.txt", "w") as file:
    file.write("CONFIDENTIAL INFORMATION\n")
    file.write("Student Name: Saumya\n")
    file.write("This file contains private data.")

print("Confidential file created successfully.")

# 2. Read the original file (plaintext)
with open("confidential.txt", "rb") as file:
    plaintext = file.read()

print("\nOriginal Plaintext:")
print(plaintext.decode("utf-8"))

# 3. Generate an encryption key
key = Fernet.generate_key()

# Save the key in a separate file
with open("secret.key", "wb") as file:
    file.write(key)

# Create a Fernet object
cipher = Fernet(key)

# 4. Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Save encrypted data to a separate file
with open("encrypted.bin", "wb") as file:
    file.write(ciphertext)

print("\nFile encrypted successfully.")
print("Encrypted data saved in encrypted.bin")

# 5. Decrypt using the correct key
with open("secret.key", "rb") as file:
    saved_key = file.read()

correct_cipher = Fernet(saved_key)

with open("encrypted.bin", "rb") as file:
    encrypted_data = file.read()

decrypted_data = correct_cipher.decrypt(encrypted_data)

# Save decrypted data to another file
with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("\nDecryption successful!")
print("Decrypted Text:")
print(decrypted_data.decode("utf-8"))

# 6. Try decrypting with an incorrect key
wrong_key = Fernet.generate_key()
wrong_cipher = Fernet(wrong_key)

try:
    wrong_cipher.decrypt(encrypted_data)
    print("Decryption with incorrect key succeeded.")
except InvalidToken:
    print("\nDecryption with incorrect key failed.")
    print("Access denied: Invalid encryption key.")
