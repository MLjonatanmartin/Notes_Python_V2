'''
Strings
    
Los strings son caracteres que entendemos por textos. Estos
son muy importantes ya que con ellos podemos trabajar con
NLP (natural language process). 

Para poder usar declarar en python un string puedes usar 
comillas simples, comillas dobles o comillas triples.

Para concatenar podemos usar el operador + o los formatos de 
f'' en el print.

Los string están indexados, por lo cual podemos acceder a ellos 
con una ubicación especifica:

# name = "Jonatan"
print(name[0]) imprime J

Si le pasamos una ubicación que no existe, nos dará un error de 
index.

Tienen distintos métodos con los cuales podemos trabajar, en caso
de que se nos olviden podemos buscarlos por internet o por la 
documentación oficial de python.

Métodos:

1) len() muestra el total de items del string.
2) .lower() coloca todo el string en minuscula.
3) .upper() coloca todo el string en mayuscula.
4) .strip() elimina los espacios entre el inicio y final.

'''

print('===' * 5)

# ejemplo de string

name = 'jonatan'
print(name)

# consulta de tipo de dato con type()

print(type(name))

print('===' * 5)

# uso del index de los strings

saludo_mundo = 'hola mundo!!!'

print(saludo_mundo[5]) # M
print(saludo_mundo[2]) # l

# para el final del string usa números negativos
print(saludo_mundo[-1]) # !

# uso del index error cuando se le pasa un index que no existe

# print(saludo_mundo[40]) # index error

print('===' * 5)

# Ejemplo de concatenar y repetir cadenas con el operador *

name = 'jonatan'
last_name = 'martin'
full_name = name + ' ' + last_name

print(full_name)

print(full_name * 3)

print('===' * 5)

# uso del método len() con string

print(len(full_name))

print('===' * 5)

# uso de métodos en string

print(full_name.upper())
print(full_name.capitalize())
print(full_name.title())

print('===' * 5)