
# Practical 8: Defining and Calling Functions

# 1. Define and call a welcome-message function
def welcome():
    print("Welcome to Python Programming!")

welcome()

# 2. Return the sum of two numbers
def add(a, b):
    return a + b

result = add(10, 20)
print("\nSum of two numbers:", result)

# 3. Calculate the area of a circle
def circle_area(radius):
    return 3.14 * radius * radius

area = circle_area(5)
print("Area of the circle:", area)

# 4. Check whether a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even_odd(8)
check_even_odd(7)

# 5. Display student details
def student_details(name, roll_no, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Course:", course)

student_details("Saumya", 101, "BCA")
