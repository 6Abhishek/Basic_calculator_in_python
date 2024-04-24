# Take input from the user
num1 = int(input("Enter the 1st number:"))  # Read 1st number as an integer
op = input("Enter the operator:")  # Read operator (+, -, *, /, %)
num2 = int(input("Enter the 2nd number:"))  # Read 2nd number as an integer

# Perform the operation based on the operator
match(op):
    case '+':
        print(num1 + num2)  # Addition
    case '-':
        print(num1 - num2)  # Subtraction
    case '*':
        print(num1 * num2)  # Multiplication
    case '/':
        print(num1 / num2)  # Division
    case '%':
        print(num1 % num2)  # Modulo
    case __:
        print("Please Enter a Valid operator")  # Invalid operator message
