# declaración de una lista

names = ['luciano', 'miku', 'vegeta']
print(names)

# Tipo de dato de una lista

print('Tipo de dato de una lista ==>',type(names))

# declaración de una lista anidada

names = ['luciano', 'miku', 'vegeta']
last_names = ['castillo', 'hatsune', 'vegita']

full_names = [names, last_names]

print(full_names)

# declaracion de una matris

coordinates = [
    [1, 1, 1],
    [2, 3, 2],
    [1, 3, 1]
]

print(coordinates)

# accediendo a un valor especifico de la matris

print(coordinates[2][1]) # 3

# declaración de una matris con más listas

coordinates_2 = [
    [[1,1,1],[1,2,1],[1,3,1]],
    [[2,2,2],[2,1,2],[2,3,2]],
    [[3,3,3],[3,1,3],[3,2,3]],
    [[4,4,4],[4,1,4],[4,2,4]],
]

print(coordinates_2)

# accediendo a un valor especifico de la lista

print(coordinates_2[2][1][0]) # 3

# declaración de una tupla

names = ('luciona', 'tommy', 'vegeta')
numbers = 1,2,3,4
word = ('a',)

print(names, numbers, word)

# tipo de dato

print(type(names), type(numbers), type(word))