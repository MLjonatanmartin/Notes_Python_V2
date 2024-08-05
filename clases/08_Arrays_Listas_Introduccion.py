# Ejemplo de una lista 

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Ejemplo de una lista con string

names = ['Jonata', 'Sophia', 'David']
print(names)

# Ejemplo de una lista con tipos de datos variados

mixed_list = [True, 1345, 'Pan con Queso', 2.97, False, None]
print(mixed_list)

# Lista con lista aninadas

vectors = [[1,2,3], [4,5,6], [7,8,9], [0,1,2]]
print(vectors)

# Ver tipo de dato con lista

print(type(vectors))

# Trabajando con métodos de las lista, algunos ejemplos

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers, len(numbers))

numbers.append(9) # Agrega el valor 9 al final
print(numbers.index(3)) # Posicion 2

numbers.remove(7) # Elimina el valor 7
print(numbers)

numbers.reverse() # Invierte el valor de la lista
print(numbers)

numbers.insert(0, 9) # Agrega el valor 9 en la posición 0
print(numbers)

print(numbers.count(9)) # Cuenta cuantas veces aparece el valor 9

# Uso de Slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)

numbers_v1 = numbers[::3] # Crea una sub-lista en salto de 3 pasos
print(numbers_v1)

numbers_v2 = numbers[1:5] # Inicia en valor 1 y termina en la posición 5
print(numbers_v2)

number_v3 = numbers[::-1] # Invierte el valor de las lista
print(number_v3)


