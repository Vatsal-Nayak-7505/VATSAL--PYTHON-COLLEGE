# Practical 7: List Operations

# Create a list of five subjects
subjects = ["Python", "Maths", "English", "Science", "Computer"]

# 1. Display the list
print("Original List:", subjects)

# 2. Access elements using indexing
print("First Subject:", subjects[0])
print("Third Subject:", subjects[2])

# 3. Modify an element
subjects[1] = "Physics"
print("After Modification:", subjects)

# 4. Add a new element
subjects.append("Chemistry")
print("After Adding:", subjects)

# 5. Remove an element
subjects.remove("English")
print("After Removing:", subjects)

# 6. Insert an element
subjects.insert(1, "Biology")
print("After Inserting:", subjects)

# 7. Pop an element
removed_subject = subjects.pop()
print("Popped Element:", removed_subject)
print("Final List:", subjects)