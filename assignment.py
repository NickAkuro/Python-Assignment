num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(f"{int(num1)} + {int(num2)} = {int(result)}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot dive by zero.")
else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")
    
    
