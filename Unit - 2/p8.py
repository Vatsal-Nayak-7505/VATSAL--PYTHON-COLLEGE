# Unit 2 - Identity Operators

# Creating two separate lists
list1 = [10, 20, 30]
list2 = [10, 20, 30]

# Creating another variable that refers to list1
list3 = list1

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

# Identity operators
print("\n----- Identity Operations -----")

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)
print("list1 is not list3 :", list1 is not list3)