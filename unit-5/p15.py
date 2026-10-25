
# Practical 15: File Types and Basic File Operations

# 1. Create and open a file using open()
file = open("student.txt", "w")

# 2. Write student details
file.write("Student Name: Saumya\n")
file.write("Roll Number: 15\n")
file.write("Course: Python Programming\n")
file.write("Unit: File Handling\n")

# 3. Close the file
file.close()
print("Student details written successfully.")

# 4. Open the file in read mode
file = open("student.txt", "r")

# 5. Read and display the contents
print("\nStudent Details:")
content = file.read()
print(content)

# 6. Close the file
file.close()
print("File closed successfully.")

# 7. Demonstrate opening the file using open()
with open("student.txt", "r") as file:
    print("Reading file using open():")
    print(file.read())
