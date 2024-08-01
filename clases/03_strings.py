# ejemplo de string

name = 'jonatan'
print(name)

# consulta de tipo de dato con type()

print(type(name))

# uso del index de los strings

saludo_mundo = 'hola mundo!!!'

print(saludo_mundo[5]) # M
print(saludo_mundo[2]) # l

# para el final del string usa números negativos
print(saludo_mundo[-1]) # !

# uso del index error cuando se le pasa un index que no existe

# print(saludo_mundo[40]) # index error

# Ejemplo de concatenar y repetir cadenas con el operador *

name = 'jonatan'
last_name = 'martin'
full_name = name + ' ' + last_name

print(full_name)

print(full_name * 3)

# uso del método len() con string

print(len(full_name))

# uso de métodos en string

print(full_name.upper())
print(full_name.capitalize())
print(full_name.title())