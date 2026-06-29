# Simple Calculator

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choosing the operation
print("\nChoose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter your choice (+, -, *, /): ")

# Performing the calculation
if operation == "+":
    result = num1 + num2
    print("Result =", result)

elif operation == "-":
    result = num1 - num2
    print("Result =", result)

elif operation == "*":
    result = num1 * num2
    print("Result =", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation! Please choose +, -, *, or /.")