# Practical 5: Type Casting

# -------- Implicit Type Casting --------

num1 = 10          # int
num2 = 5.5         # float

result = num1 + num2

print("Implicit Type Casting:")
print("Value:", result)
print("Data Type:", type(result))


# -------- Explicit Type Casting --------

# Integer to Float
a = 10
b = float(a)

print("\nInteger to Float:")
print("Value:", b)
print("Data Type:", type(b))


# String to Integer
age = "18"
age_int = int(age)

print("\nString to Integer:")
print("Value:", age_int)
print("Data Type:", type(age_int))


# Integer to String
number = 100
number_str = str(number)

print("\nInteger to String:")
print("Value:", number_str)
print("Data Type:", type(number_str))