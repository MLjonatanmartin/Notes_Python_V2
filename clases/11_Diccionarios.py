# Declaración de un diccionario

from click import edit


information = {
    'nombre' : 'juan',
    'apellido' : 'martin',
    'altura': 1.78
}

print(information)

# obtener un valor en especifico

print(information['nombre'])

# obetener las llaves del diccionario

print('obetener las llaves =>', information.keys())

# obtener los valores del diccionario

print('obtener los valores =>', information.values())

# obtener las palabras claves y valores de un diccionario en tuplas

print('obtener clave y valor en tuplas =>', information.items())

# diccionario con un diccionario dentro y con listas

books = {
    'Stephen King' : {
        'titulo' : ['Carrie', 'El resplandor', 'it'],
        'publicacion': [1974, 1977, 1986],
        'editorial' : ['doubleday', 'diybleday', 'vivking press']
    }
}

print('accediendo a su tercer libro')
print(books['Stephen King']['titulo'][2]) # imprime it

# ejemplo de un diccionario guardando funciones

operations = {
    'sum' : lambda x,y: x + y,
    'sub' : lambda x,y: x - y,
    'mul' : lambda x,y: x * y,
    'div' : lambda x,y: x / y if y > 0 else 'No se puede dividir entre 0'
}

print('suma 7 + 5 =',operations['sum'](7,5))
print('resta 15 - 5 =',operations['sub'](15,5))
print('multiplicación 30x4 =',operations['mul'](30,4))
print('división 10 / 2 =',operations['div'](10,2))
print('división entre 0 ==> 10 + 0 =',operations['div'](10,0))