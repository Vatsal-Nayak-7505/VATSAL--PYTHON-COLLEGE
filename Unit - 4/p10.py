
# Practical 10: Returning Single and Multiple Values

# 1. Return the square of a number
def square(number):
    return number * number

print("Square of 5:", square(5))

# 2. Return the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print("\nMaximum of 10 and 20:", maximum(10, 20))

# 3. Return sum, difference, product, and quotient
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    return total, difference, product, quotient

results = calculate(20, 10)
print("\nCalculation Results:", results)

# 4. Unpack multiple returned values into variables
total, difference, product, quotient = calculate(20, 10)

print("\nUnpacked Values:")
print("Sum:", total)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# 5. Calculate total marks and percentage
def calculate_marks(marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)
    return total_marks, percentage

marks = [85, 90, 78, 88, 92]
total_marks, percentage = calculate_marks(marks)

print("\nStudent Marks:", marks)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")

# 6. Use a returned value in another calculation
def add(a, b):
    return a + b

def double(number):
    return number * 2

result = double(add(10, 20))
print("\nDouble of the sum of 10 and 20:", result)

# 7. Compare print() and return
def using_print():
    print("Hello from print()")

def using_return():
    return "Hello from return"

print("\nUsing print():")
value1 = using_print()
print("Returned value:", value1)

print("\nUsing return:")
value2 = using_return()
print("Returned value:", value2)
