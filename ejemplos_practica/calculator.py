"""
Implementarion of a basic calculator to perform arithmetic operations
"""

operations = ['+', '-', 'x', '/']

user_operation = input("Write your operation\n")
num1 = []
num2 = []
operation = []
after_operator = False

for i in user_operation:
    if i in operations: 
        operation.append(i)
        after_operator= True
    else:
        if after_operator:
            num2.append(i)
        else:
            num1.append(i)

num1_int = int("".join(num1))
operation_str = "".join(operation)
num2_int = int("".join(num2))


def calculator(num1, operation, num2):
    
    calculation = {
        "sum": lambda num1, num2: num1 + num2 ,
        "subs": lambda num1, num2: num1 - num2 ,
        "multi": lambda num1, num2: num1 * num2,
        "div": lambda num1, num2: num1 / num2
    }

    if operation in operations:
        
        if operation == "+":
            result = calculation["sum"](num1, num2)
            print(result)
        
        elif operation == "-":
            result = calculation["subs"](num1, num2)
            print(result)

        elif operation == "x":
            result = calculation["multi"] (num1, num2)
            print(result)

        else:
            if num2 <= 0:
                print("Error, you can't divide number in zero")
            else:
                result = calculation["div"] (num1, num2)
                print(result)


calculator(num1_int, operation_str, num2_int)

