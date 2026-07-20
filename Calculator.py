def get_numbers():
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))
    return num1, num2

def get_operation():
    valid_operations = ["+", "-", "*", "/", "**"]
    operation = input("Enter an operation (+, -, *, /, **) :")

    while operation not in valid_operations:
        operation = input("Invalid. Enter valid operations to perform(+, -, *, /, **) :")

    return operation

def calculate(num1, num2, operation):
    if operation == "+":
        return(num1 + num2)        
    elif operation == "-":
        return(num1 - num2)    
    elif operation == "*":
        return(num1 * num2)    
    elif operation == "/":
        if num2 == 0:
            return("Error, Cannot divide by zero")
        else:
            return(num1 / num2)    
    elif operation == "**":
        return(num1 ** num2)
    else:
        return("Invalid Syntax")

while True:
    num1, num2 = get_numbers()
    operation = get_operation()
    result = calculate(num1, num2, operation)
    print(num1, operation, num2, "=", result)

    again = input("Do you want to calculate again? (yes/no) :").lower()
    if again != "yes":
        print("Thanks for using the calculator")
        break