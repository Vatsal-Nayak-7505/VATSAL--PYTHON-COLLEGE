
# Practical 13: Creating a Custom Module

# 1 and 2. Define calculator functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# 7. Demonstrate the main block
if __name__ == "__main__":
    print("Calculator Module")

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
