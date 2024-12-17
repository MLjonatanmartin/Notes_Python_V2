# declaracion de un ciclo for

numbers = [x for x in range(1,50,3)]

for i in numbers:
    (print(i, end=' '))
else:
    print('Zzz')

# ciclo con una lista de strings

fuits = ['apple', 'orange', 'watermelon', 'banana', 'pineapple']

for fruit in fuits:
    print(fruit.upper(), end=' ')

# ciclo while

num = 7

while (num != 10):
    num -= 1
    num += 2
    print(num)



