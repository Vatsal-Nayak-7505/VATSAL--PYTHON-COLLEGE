
# Practical 2: List Methods and Membership

# 1. Create a list of student names
students = ["Amit", "Priya", "Rahul", "Neha", "Priya"]
print("Original List:", students)

# 2. Demonstrate append(), extend(), and insert()
students.append("Karan")
print("After append():", students)

students.extend(["Sneha", "Rohit"])
print("After extend():", students)

students.insert(1, "Anjali")
print("After insert():", students)

# 3. Demonstrate remove(), pop(), and clear()
students.remove("Rahul")
print("After remove():", students)

removed_student = students.pop()
print("Popped Student:", removed_student)
print("After pop():", students)

# 4. Demonstrate sort(), reverse(), index(), and count()
students.sort()
print("After sort():", students)

students.reverse()
print("After reverse():", students)

print("Index of Priya:", students.index("Priya"))
print("Count of Priya:", students.count("Priya"))

# 5. Search using in and not in
print("Is Amit in the list?", "Amit" in students)
print("Is Rahul not in the list?", "Rahul" not in students)

# Demonstrate clear() on a separate list
students_copy = students.copy()
students_copy.clear()
print("After clear():", students_copy)
