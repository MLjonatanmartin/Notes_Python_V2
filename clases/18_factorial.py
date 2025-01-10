# Intento de hacer mi factorial

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
number_factorial = factorial(6) 

print(number_factorial)

# con ciclo for

def factorial_ciclo(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

number_factorial = factorial_ciclo(5)
print(number_factorial)

# Recursividad con el número de Fignachi

def figonachi(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return figonachi(number - 1) + figonachi(number - 2)
    
number_fibonachi = figonachi(0)
print(number_fibonachi)