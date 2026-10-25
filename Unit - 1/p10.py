# Practical 10: List Operations

numbers = []

# Accept 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find maximum and minimum
maximum = max(numbers)
minimum = min(numbers)

# Calculate sum and average
total = sum(numbers)
average = total / 10

# Display results
print("\n----- Results -----")
print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
print("Average:", average)

# Display even and odd numbers
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)