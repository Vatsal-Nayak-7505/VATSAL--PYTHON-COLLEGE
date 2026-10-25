
# Practical 4: Creating and Accessing Tuples

# 1. Create tuples with different data types
student = ("Saumya", 20, 85.5, True)
print("Tuple with different data types:", student)

# 2. Create empty and single-element tuples
empty_tuple = ()
single_tuple = (10,)
print("Empty Tuple:", empty_tuple)
print("Single-element Tuple:", single_tuple)

# 3. Access items using positive and negative indexing
numbers = (10, 20, 30, 40, 50)
print("\nOriginal Tuple:", numbers)
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])
print("Second last element:", numbers[-2])

# 4. Extract elements using slicing
print("\nSliced Tuple (index 1 to 3):", numbers[1:4])

# 5. Traverse a tuple using a loop
print("\nTraversing the Tuple:")
for item in numbers:
    print(item)

# 6. Demonstrate tuple immutability
print("\nDemonstrating Tuple Immutability:")
try:
    numbers[0] = 100
except TypeError:
    print("Error: Tuple elements cannot be changed.")

print("Tuple remains unchanged:", numbers)

# 7. Compare tuples and lists
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

print("\nTuple:", my_tuple)
print("List:", my_list)

my_list[0] = 100
print("List after modification:", my_list)
print("Tuple remains unchanged:", my_tuple)
