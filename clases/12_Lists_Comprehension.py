# Ejemplo de una list comprehension 

squares = [x**2 for x in range(1,5)]
print(squares)

# sacando una solo posición

print(squares[0])

# conviertiendo de celsius a farenheit

celcius = [0, 20, 40, 37]
fahrenheit = [(9//5 * c) + 32 for c in celcius]

print('temperatura en F:', fahrenheit) 

# Lista de números pares

odd_numbers = [x for x in range(1,11) if (x % 2) != 0]
print(odd_numbers)

even_numbers = [x for x in range(1,11) if (x % 2) == 0]
print(even_numbers)


# hacer una transpuesta de una matriz

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

