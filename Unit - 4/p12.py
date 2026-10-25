
# Practical 12: Anonymous Functions (Lambda)

# 1. Create a lambda to add two numbers
add = lambda a, b: a + b
print("Sum of two numbers:", add(10, 20))

# 2. Create a lambda to square a number
square = lambda n: n * n
print("Square of 5:", square(5))

# 3. Find the maximum of two values using lambda
maximum = lambda a, b: a if a > b else b
print("Maximum of 15 and 25:", maximum(15, 25))

# 4. Use map() and lambda for squares
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))
print("\nOriginal Numbers:", numbers)
print("Squares using map():", squares)

# 5. Use filter() and lambda for even numbers
values = [10, 15, 20, 25, 30, 35, 40]
even_numbers = list(filter(lambda n: n % 2 == 0, values))
print("\nOriginal Values:", values)
print("Even Numbers using filter():", even_numbers)

# 6. Sort student records by marks using sorted() and lambda
students = [
    ("Amit", 75),
    ("Priya", 92),
    ("Rahul", 68),
    ("Neha", 85)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("\nStudents Sorted by Marks:")
for student in sorted_students:
    print(student[0], "-", student[1])

# 7. Compare lambda with def
def multiply(a, b):
    return a * b

multiply_lambda = lambda a, b: a * b

print("\nUsing def:", multiply(4, 5))
print("Using lambda:", multiply_lambda(4, 5))
