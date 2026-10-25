
# Practical 5: Creating and Accessing Dictionaries

# 1. Create a student dictionary
student = {
    "roll_no": 101,
    "name": "Saumya",
    "course": "BCA",
    "marks": 85
}
print("Student Dictionary:", student)

# 2. Access values using keys and get()
print("\nAccessing Values:")
print("Roll Number:", student["roll_no"])
print("Name:", student["name"])
print("Course:", student.get("course"))
print("Marks:", student.get("marks"))

# 3. Add a key-value pair and update a value
student["city"] = "Ahmedabad"
print("\nAfter Adding City:", student)

student["marks"] = 90
print("After Updating Marks:", student)

# 4. Delete an item using del and pop()
del student["city"]
print("\nAfter Using del:", student)

removed_course = student.pop("course")
print("Removed Course:", removed_course)
print("After Using pop():", student)

# 5. Traverse using keys(), values(), and items()
print("\nDictionary Keys:")
for key in student.keys():
    print(key)

print("\nDictionary Values:")
for value in student.values():
    print(value)

print("\nDictionary Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# 6. Demonstrate update(), setdefault(), and clear()
student.update({"course": "BCA", "marks": 95})
print("\nAfter update():", student)

student.setdefault("grade", "A")
print("After setdefault():", student)

# Use clear() on a copy to preserve the original dictionary
student_copy = student.copy()
student_copy.clear()
print("After clear():", student_copy)
