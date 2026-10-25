
# Practical 1: List Operations

# 1. Create a list of 10 student marks
marks = [85, 72, 90, 65, 78, 88, 56, 95, 69, 82]

print("Student Marks:", marks)

# 2. Access elements using positive and negative indexes
print("\nPositive Indexing:")
print("First mark:", marks[0])
print("Third mark:", marks[2])

print("\nNegative Indexing:")
print("Last mark:", marks[-1])
print("Second last mark:", marks[-2])

# 3. Display a range using slicing
print("\nSlicing (index 2 to 5):", marks[2:6])

# 4. Traverse using for loop
print("\nTraversing using for loop:")
for mark in marks:
    print(mark)

# Traverse using while loop
print("\nTraversing using while loop:")
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# 5. Display each element with its index
print("\nMarks with their indexes:")
for i in range(len(marks)):
    print("Index", i, ":", marks[i])
