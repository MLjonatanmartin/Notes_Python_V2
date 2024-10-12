"""
Implementarion ofa a basic calculator to perform arithmetic operations
"""

operations = ['+', '-', 'x', '/']

num1, operation, num2 = input("write your operation\n")

def calculator(num1, operation, num2):
    """
    docstring
    """
    
    calculation = {
        "sum": lambda num1, num2: num1 + num2 ,

    }

    if operation in operations:
        st