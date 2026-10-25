# Unit 2 - Pass Statement

# Using pass inside an if statement
num = 10

if num > 0:
    pass
else:
    print("Number is not positive")

print("Program continued after if statement")


# Using pass inside a loop
print("\nNumbers from 1 to 5:")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)