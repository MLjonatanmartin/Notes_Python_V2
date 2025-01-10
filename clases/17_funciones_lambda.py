# Declaración de una función Lambda

add = lambda x, y: x + y

print(add(5, 3))

# Declaración de una función Lambda con valores por defecto

subs = lambda x=2, y=1: x - y

print(subs(80,90))

# Uso de map() con una función Lambda

numbers = range(27)

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Uso de filter() con una función Lambda

even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
