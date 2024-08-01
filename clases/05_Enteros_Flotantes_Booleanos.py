"""
Tipos de datos:

Para trabajar con la programación es importante
conocer sobre los tipos de datos. EN los tipos de datos
tenemos:

1) String = str

    Son cadenas de caracteres.

2) Intreger = int

    Son los números sin decimal.

3) Float = float

    Son los números decimales.

4) Boolean = bool

    Son el valor True or False para controlar la lógica
    y el flujo de un programa. 


Anotación científica:

Sirve para escribir números muy grandes o muy pequeños de manera
compacta. Para realizar anotaciones cientificas en Python, se hace de la 
siguiente manera:

1) 1e6 = 1000000
2) 1e-6 = 0.000001

Nota: Los números con anotación cientifica los escribe en tipo float

"""

print('===' * 5)

# ejemplo de número con anotación cientifica

num_1 = 30e7
num_2 = 30e-7

print(num_1, 'tipo =>', type(num_1))
print(num_2, 'tipo =>', type(num_2))

print('===' * 5)

# ejemplo de int

x = 10 

print(x, 'type =>', type(x))

print('===' * 5)

# ejemplo de float

y = 5.678

print(y, 'type =>', type(y))

print('===' * 5)

# Ejemplo de operaciones aritmeticas

suma_1 = x + x
suma_2 = y + y
suma_3 = x + y

print(suma_1, 'type =>', type(suma_1))
print(suma_2, 'type =>', type(suma_2))
print(suma_3, 'type =>', type(suma_3))

print('===' * 5)

# ejemplo de booleanos

is_true = True
is_false = False

print(is_true, 'type =>', type(is_true))
print(is_false, 'type =>', type(is_false))

print('===' * 5)