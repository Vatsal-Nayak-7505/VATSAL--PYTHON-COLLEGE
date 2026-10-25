
# Practical 17: Writing, Appending and Managing Files

import os

# 1. Write multiple student records
with open("students.txt", "w") as file:
    file.write("Saumya\n")
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")

print("Student records written successfully.")

# 2. Append a new record
with open("students.txt", "a") as file:
    file.write("Neha\n")

print("New student record appended successfully.")

# 3. Read line by line and number records
print("\nStudent Records:")
with open("students.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

# 4. Count lines, words, and characters
with open("students.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("\nTotal lines:", len(lines))
print("Total words:", len(words))
print("Total characters:", characters)

# 5. Search for a student name
search_name = input("\nEnter student name to search: ")

if search_name in lines:
    print(search_name, "found in the file.")
else:
    print(search_name, "not found in the file.")

# 6. Check file existence using os
if os.path.exists("students.txt"):
    print("\nstudents.txt exists.")
else:
    print("\nstudents.txt does not exist.")

# 7. Create a test file
with open("testfile.txt", "w") as file:
    file.write("This is a test file.")

# Rename the test file
if os.path.exists("testfile.txt"):
    if not os.path.exists("renamed_testfile.txt"):
        os.rename("testfile.txt", "renamed_testfile.txt")
        print("Test file renamed successfully.")
    else:
        print("Rename skipped: destination already exists.")

# Delete the renamed test file
if os.path.exists("renamed_testfile.txt"):
    os.remove("renamed_testfile.txt")
    print("Test file deleted successfully.")
