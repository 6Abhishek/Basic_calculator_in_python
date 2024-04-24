
num1 = int(input("Enter the 1st number:"))
op = input("Enter the operator:")
num2 = int(input("Enter the 2nd number:"))

match(op):
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case '%':
        print(num1%num2)
    case __:
        print("Please Enter a Valid operator")