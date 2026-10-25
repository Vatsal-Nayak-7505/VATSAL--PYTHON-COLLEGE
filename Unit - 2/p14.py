# Unit 2 - Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (+, -, *, /): ")

if choice == "+":
    print("Result =", num1 + num2)

elif choice == "-":
    print("Result =", num1 - num2)

elif choice == "*":
    print("Result =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid Choice!")