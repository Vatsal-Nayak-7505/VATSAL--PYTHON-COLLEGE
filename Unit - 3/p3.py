
# Practical 3: List Comprehensions

# 1. Generate squares from 1 to 20
squares = [n ** 2 for n in range(1, 21)]
print("Squares from 1 to 20:", squares)

# 2. Generate even numbers from 1 to 50
even_numbers = [n for n in range(1, 51) if n % 2 == 0]
print("\nEven numbers from 1 to 50:", even_numbers)

# 3. Create numbers divisible by 5
divisible_by_5 = [n for n in range(1, 51) if n % 5 == 0]
print("\nNumbers divisible by 5:", divisible_by_5)

# 4. Convert words to uppercase
words = ["python", "list", "computer", "programming"]
uppercase_words = [word.upper() for word in words]
print("\nUppercase words:", uppercase_words)

# 5. Select marks greater than or equal to 40
marks = [25, 67, 38, 90, 45, 32, 78, 40]
passed_marks = [mark for mark in marks if mark >= 40]
print("\nMarks greater than or equal to 40:", passed_marks)
