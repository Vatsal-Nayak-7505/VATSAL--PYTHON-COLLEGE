
# Practical 7: Set Methods and Collection Comparison

# 1. Demonstrate add() and update()
set1 = {10, 20, 30}
set1.add(40)
print("After add():", set1)

set1.update([50, 60])
print("After update():", set1)

# 2. Demonstrate remove(), discard(), and pop()
set1.remove(20)
print("\nAfter remove():", set1)

set1.discard(100)  # No error if the element is absent
print("After discard():", set1)

removed_element = set1.pop()
print("Popped Element:", removed_element)
print("After pop():", set1)

# 3. Demonstrate set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nUnion:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference (A - B):", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

# 4. Demonstrate issubset(), issuperset(), and isdisjoint()
X = {2, 3}
Y = {1, 2, 3, 4, 5}
Z = {6, 7}

print("\nIs X a subset of Y?", X.issubset(Y))
print("Is Y a superset of X?", Y.issuperset(X))
print("Are X and Z disjoint?", X.isdisjoint(Z))

# 5. Demonstrate clear()
set_copy = A.copy()
set_copy.clear()
print("\nAfter clear():", set_copy)

# 6. Store student roll numbers in different collections
roll_list = [101, 102, 103, 101]
roll_tuple = (101, 102, 103, 101)
roll_dictionary = {
    101: "Amit",
    102: "Priya",
    103: "Rahul"
}
roll_set = {101, 102, 103, 101}

print("\nStudent Roll Numbers:")
print("List:", roll_list)
print("Tuple:", roll_tuple)
print("Dictionary:", roll_dictionary)
print("Set:", roll_set)

# Demonstrate accessing elements
print("\nAccessing Elements:")
print("First roll number in list:", roll_list[0])
print("First roll number in tuple:", roll_tuple[0])
print("Student with roll number 102:", roll_dictionary[102])
print("Is roll number 103 in set?", 103 in roll_set)

# 7. Compare collections
print("\nCollection Comparison:")
print("List allows duplicates and is mutable.")
print("Tuple allows duplicates and is immutable.")
print("Dictionary stores unique keys with associated values.")
print("Set stores unique elements and is mutable.")
