# Declaración de una lista

numbers = [1, 2, 3, 4, 5]

# Creación de un iterador

my_iter = iter(numbers)

# Uso de la función next()

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Uso de un iterador con un ciclo for

greetings = "Hello world"

# creando el objeto iterador

my_iter_greetings = iter(greetings)

# iterar en la cadena

for letter in my_iter_greetings:
    print(letter, end='')
else:
    print('\nIteración terminada')


# Creación de un ciclo para números impares

limit = 14

odd_itter = iter(range(1, limit+1, 2))

for odd in odd_itter:
    print(odd, end=' ')
else:
    print('\nIteración terminada')

# Creación de un generador

def my_generator():
    yield 1
    yield 2
    yield 3

# Uso de un generador

for value in my_generator():
    print(value, end=' ')
else:
    print('\nIteración terminada')

# Ejemplo de la generación de Fibonacci

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for value in fibonacci(100):
    print(value, end=' ')
else:
    print('\nIteración terminada')


