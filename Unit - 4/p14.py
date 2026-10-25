
# Practical 14: Standard Python Modules

# Import standard modules
import math
import random
import datetime
import calendar
import os
import statistics

# 1. Use math module
print("1. MATH MODULE")
print("Square root of 25:", math.sqrt(25))
print("Power (2^3):", math.pow(2, 3))
print("Factorial of 5:", math.factorial(5))

# 2. Use random module
print("\n2. RANDOM MODULE")
print("Random integer:", random.randint(1, 100))
print("Random number between 0 and 1:", random.random())

# 3. Use datetime module
print("\n3. DATETIME MODULE")
current_date = datetime.datetime.now()
print("Current Date and Time:", current_date.strftime("%d-%m-%Y %H:%M:%S"))
print("Current Date:", current_date.strftime("%d-%m-%Y"))

# 4. Use calendar module
print("\n4. CALENDAR MODULE")
print(calendar.month(2026, 10))

# 5. Use os module
print("5. OS MODULE")
print("Current Directory:", os.getcwd())
print("Directory Contents:", os.listdir())

# 6. Use statistics module
print("\n6. STATISTICS MODULE")
marks = [70, 80, 80, 90, 100]
print("Marks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))

# 7. Combine random and datetime modules
print("\n7. RANDOM STUDENT ID AND DATE")
student_id = "STU" + str(random.randint(1000, 9999))
today = datetime.datetime.now().strftime("%d-%m-%Y")

print("Random Student ID:", student_id)
print("Registration Date:", today)
