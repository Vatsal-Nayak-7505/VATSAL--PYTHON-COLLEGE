
# Practical 9: Function Parameters and Arguments

# 1. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

print("1. Positional Arguments:")
student("Saumya", 20)

# 2. Keyword Arguments
def display_student(name, course):
    print("\nName:", name)
    print("Course:", course)

print("\n2. Keyword Arguments:")
display_student(course="BCA", name="Saumya")

# 3. Default Arguments
def greet(name, message="Welcome to Python!"):
    print(message, name)

print("\n3. Default Arguments:")
greet("Saumya")
greet("Rahul", "Good morning,")

# 4. Variable-Length Arguments using *args
def add_numbers(*args):
    print("\nNumbers:", args)
    print("Sum:", sum(args))

print("\n4. *args Example:")
add_numbers(10, 20, 30, 40)

# 5. Variable-Length Keyword Arguments using **kwargs
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print("\n5. **kwargs Example:")
student_info(name="Saumya", course="BCA", roll_no=101)

# 6. Calculate student total using variable-length arguments
def calculate_total(name, *marks):
    total = sum(marks)
    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Total Marks:", total)

print("\n6. Student Total:")
calculate_total("Saumya", 85, 90, 78, 88, 92)

# 7. Compare argument types
print("\n7. Comparison of Argument Types:")
print("Positional: Values are passed according to position.")
print("Keyword: Values are passed using parameter names.")
print("Default: A parameter uses a predefined value if omitted.")
print("*args: Accepts multiple positional arguments.")
print("**kwargs: Accepts multiple keyword arguments.")
