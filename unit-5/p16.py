
# Practical 16: File Modes and File Reading

# 1. Use w mode to create and write a file
with open("student.txt", "w") as file:
    file.write("Saumya - Python\n")
    file.write("Rahul - Java\n")

print("File created and data written.")

# 2. Use r mode to read the file
try:
    with open("student.txt", "r") as file:
        print("\nReading using read():")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")

# 3. Demonstrate overwrite behaviour using w mode
with open("student.txt", "w") as file:
    file.write("Priya - C++\n")

print("File overwritten using w mode.")

# 4. Append records using a mode
with open("student.txt", "a") as file:
    file.write("Amit - Python\n")
    file.write("Neha - Java\n")

print("Records appended successfully.")

# 5. Read using readline()
with open("student.txt", "r") as file:
    print("\nReading using readline():")
    print(file.readline(), end="")
    print(file.readline(), end="")

# 6. Read using readlines()
with open("student.txt", "r") as file:
    print("\n\nReading using readlines():")
    lines = file.readlines()
    print(lines)

# 7. Use x mode to create a new file
try:
    with open("newstudent.txt", "x") as file:
        file.write("New Student: Karan\n")
    print("\nFile created using x mode.")
except FileExistsError:
    print("\nError: newstudent.txt already exists.")

# 8. Binary writing using wb
with open("data.bin", "wb") as file:
    file.write(b"Python File Handling")

print("Binary data written successfully.")

# 9. Binary reading using rb
with open("data.bin", "rb") as file:
    binary_data = file.read()
    print("Binary data:", binary_data)
