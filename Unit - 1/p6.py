# Practical 6: String Operations

# Creating strings
first_name = "Saumya"
last_name = "Singh"

# 1. Find string length
print("Length of first name:", len(first_name))

# 2. Convert to uppercase and lowercase
print("Uppercase:", first_name.upper())
print("Lowercase:", first_name.lower())

# 3. Access characters using indexing
print("First character:", first_name[0])
print("Third character:", first_name[2])

# 4. String slicing
print("Sliced string:", first_name[0:4])

# 5. Concatenate two strings
full_name = first_name + " " + last_name
print("Full Name:", full_name)