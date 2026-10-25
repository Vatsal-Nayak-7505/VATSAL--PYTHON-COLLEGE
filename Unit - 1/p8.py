# Practical 8: Traversing a List

subjects = ["Python", "Maths", "English", "Science", "Computer"]

# Using for loop
print("Using for loop:")

for subject in subjects:
    print(subject)


# Using while loop
print("\nUsing while loop:")

i = 0

while i < len(subjects):
    print(subjects[i])
    i += 1