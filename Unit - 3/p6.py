
# Practical 6: Creating Sets and Set Operations

# 1. Create sets using set() and set literals
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])

print("Set using literal:", set1)
print("Set using set():", set2)

# 2. Distinguish an empty set from an empty dictionary
empty_set = set()
empty_dictionary = {}

print("\nEmpty Set:", empty_set)
print("Empty Dictionary:", empty_dictionary)
print("Type of empty set:", type(empty_set))
print("Type of empty dictionary:", type(empty_dictionary))

# 3. Remove duplicates from a list using a set
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)

print("\nOriginal List:", numbers)
print("List after removing duplicates:", unique_numbers)

# 4. Demonstrate set operations
print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 5. Check subsets and supersets
small_set = {2, 3}
large_set = {1, 2, 3, 4, 5}

print("\nIs small_set a subset?", small_set.issubset(large_set))
print("Is large_set a superset?", large_set.issuperset(small_set))

# 6. Check membership using in
print("\nIs 3 in set1?", 3 in set1)
print("Is 10 in set1?", 10 in set1)

# 7. Apply set operations to student-participant lists
event1 = ["Amit", "Priya", "Rahul", "Neha"]
event2 = ["Priya", "Neha", "Karan", "Sneha"]

participants1 = set(event1)
participants2 = set(event2)

print("\nEvent 1 Participants:", participants1)
print("Event 2 Participants:", participants2)
print("All Participants:", participants1.union(participants2))
print("Participants in Both Events:", participants1.intersection(participants2))
print("Only in Event 1:", participants1.difference(participants2))
print("Participants in Exactly One Event:",
      participants1.symmetric_difference(participants2))
