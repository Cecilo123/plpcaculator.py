
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if '.' in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

if '.' in num2:
    num2 = float(num2)
else:
    num2 = int(num2)

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation! Please use +, -, *, or /.")
