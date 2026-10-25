
# Practical 18: Password-Protected File Access

import os
import getpass

# Stored password for demonstration only
stored_password = "Saumya123"

# 1. Create a confidential text file
with open("confidential.txt", "w") as file:
    file.write("CONFIDENTIAL INFORMATION\n")
    file.write("Student Name: Saumya\n")
    file.write("Department: Computer Science\n")
    file.write("This information is protected.\n")

print("Confidential file created successfully.")

# 2. Limit repeated failed attempts
max_attempts = 3
authenticated = False

for attempt in range(max_attempts):
    try:
        password = getpass.getpass("Enter password: ")

        # 3. Compare entered password with stored password
        if password == stored_password:
            authenticated = True
            print("\nAuthentication successful!")
            break
        else:
            remaining = max_attempts - attempt - 1
            print("Access denied. Incorrect password.")

            if remaining > 0:
                print("Attempts remaining:", remaining)

    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        break

# 4. Display contents only after successful authentication
if authenticated:
    try:
        if os.path.exists("confidential.txt"):
            with open("confidential.txt", "r") as file:
                print("\nConfidential File Contents:")
                print(file.read())
        else:
            print("Error: Confidential file not found.")

    except OSError:
        print("Error: Unable to read the file.")
else:
    print("\nAccess denied. Maximum attempts reached or login cancelled.")
