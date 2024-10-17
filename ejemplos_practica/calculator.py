"""
Implementarion of a basic calculator to perform arithmetic operations
"""

operations = ['+', '-', 'x', '/']

num_user1, operation, num_user2 = input("write your operation\n")

num1 = int(num_user1)
num2 = int(num_user2)

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
            if num2 > 0:
                print("Error, you can't divide number in zero")
            else:
                result = calculation["div"] (num1, num2)
                print(result)


calculator(num1, operation, num2)

