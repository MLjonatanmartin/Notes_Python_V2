---
# Notes_Python_V2
---

Estos son mis apuntes de **Python** de la escuela de Platzi. En este 
repositorio tendré a la mano las notas importantes para cuando olvide
cosas de Python. Por otro lado, tendré una carpeta de ejercicios de 
práctica relacionado con los temas que vea en clase. 

---

# Clase #1 

## Conceptos básicos de la programación.

1). Sintaxis: cada lenguaje tiene su sintaxtis que determina como se 
    escribe el código. Es bastante común cometer errores sobre la sitaxis.

2). Semántica: Es la consistencia y significa en el código. Si
    trabajamos con números, tanto los inputs como los outputs
    deben de ser números para mantener la coherencia en el código. 

3). Variables: Son como cajas para guardar información, guardar datos. 
    En POO y cosas más avanzadas son referencias de punteros a objetos
    en memoria. 

    En los lenguajes de programación hay palabras reservadas, por lo que
    esas palabras no se pueden usar para nombrar variables. 

    Las variables a lo largo del código se les puede cambiar de valor
    reasingar.

# Clase #2

## Strings
    
Los strings son caracteres que entendemos por textos. Estos
son muy importantes ya que con ellos podemos trabajar con
NLP (natural language process). 

Para poder usar declarar en python un string puedes usar 
comillas simples, comillas dobles o comillas triples.

Para concatenar podemos usar el operador + o los formatos de 
f'' en el print.

Los string están indexados, por lo cual podemos acceder a ellos 
con una ubicación especifica:

```
# name = "Jonatan"
print(name[0]) imprime J
```

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

# Clase 3

## Tipos de datos:

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

# Clase 4

## Print y sus usos

Print es una herramienta poderosa e importante, ya que al final
del día la vamos a usar a lo largo de nuestro código casi todo 
el tiempo. 

Print es la puerta de entrada a la comunicación de tus programas 
con el mundo exterior.

Métodos Básicos de print:

1) Usando lo para imprimir en consola mensajes, variables, funciones,
datos, etc.

2) Concatenar:

    Existen varias maneras para hacerlo:

    1) uso del operador +:

        Cuando usas este operador, une las cosas tal cual están
        sin agruegar espacios. Recuerda agregar espacios para que
        quede realmente bien.

3) Uso de la coma:

    Con la coma puedes unir cosas para que se impriman en la misma
    expresión de print. Cuando la usas, te coloca un espacio por 
    defecto.

4) Uso de sep:

    sintaxis: sep="value"

    Con este metodo puedes controlar la separación de los valores con 
    las comas. De esta manera tendrás impreso las varibles impresas
    separadas con el caracter que te guste.

5). Uso del end:

    sintaxis end="value"

    Cuando print termina de imprimir algo, siempre al final agrega un 
    salto de línea, para que otra cosa se imprima en la siguiente
    línea en la parte de abajo. 

    Para cambiar eso podemos usar end y con eso controlar el comportamiento
    al final cuando algo se termine de imprimir
        

6) Uso de formatos con f-stings:

    Podemos imprimir varias cosas y de distintas manera, atención a los
    siguiente métodos:

    1). Most Common:

        f'{} {}'

        con este método puedes imprimir texto y variable/funciones, en los
        corchetes colocas las variables/funciones. El texto lo puedes poner
        antes o después de un corchete, 

# Clase 5