
# Practical 11: Variable Scope and Recursive Functions

# 1. Demonstrate local and global variables
x = 100  # Global variable

def show_variables():
    x = 50  # Local variable
    print("Local variable x:", x)

show_variables()
print("Global variable x:", x)

# 2. Access a global variable inside a function
message = "Welcome to Python"

def display_message():
    print("\nGlobal message:", message)

display_message()

# 3. Use the global keyword
count = 10

def update_count():
    global count
    count = count + 5

update_count()
print("\nUpdated global count:", count)

# 4. Calculate factorial recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))

# 5. Calculate sum of first n natural numbers recursively
def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)

print("Sum of first 10 natural numbers:", natural_sum(10))

# 6. Generate Fibonacci numbers recursively
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")

print()

# 7. Explain the need for a base condition
print("\nA base condition stops recursion.")
print("Without it, recursive calls may continue until an error occurs.")
