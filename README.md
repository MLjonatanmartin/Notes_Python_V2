---
# Notes_Python_V2
---

Estos son mis apuntes de **Python** de la escuela de Platzi. En este
repositorio tendré a la mano las notas importantes para cuando olvide 
cosas de Python. Por otro lado, tendré una carpeta de 
**ejercicios de práctica** relacionados con los temas que vea en clase.

---

# Clase #2

## Conceptos básicos de la programación

1. **Sintaxis**: Cada lenguaje tiene su sintaxis que determina cómo se
escribe el código. Es bastante común cometer errores sobre la sintaxis.

2. **Semántica**: Es la consistencia y el significado en el código. Si
trabajamos con números, tanto los *inputs* como los *outputs* deben de 
ser números para mantener la coherencia en el código.

3. **Variables**: Son como cajas para guardar información o datos. En POO 
y cosas más avanzadas, son referencias de punteros a objetos en memoria. En
los lenguajes de programación hay palabras reservadas, por lo que esas
palabras no se pueden usar para nombrar variables. Las variables a lo 
largo del código se les puede cambiar de valor reasignar.

---

# Clase #3

## Strings

Los strings son caracteres que entendemos por textos. Estos son muy
importantes ya que con ellos podemos trabajar con NLP (Natural Language
Processing).

Para poder usar y declarar un string en Python puedes usar comillas simples,
comillas dobles o comillas triples.

Para concatenar podemos usar el operador `+` o los formatos de `f''` 
en el `print`.

Los strings están indexados, por lo cual podemos acceder a ellos con una
ubicación específica:

`name = "Jonatan"`

`print(name[0])  # imprime J`

Si le pasamos una ubicación que no existe, nos dará un error de index.

Tienen distintos métodos con los cuales podemos trabajar. En caso de que se
nos olviden, podemos buscarlos por internet o por la documentación oficial 
de Python.

**Métodos**:

1. `len()` muestra el total de items del string.
2. `.lower()` coloca todo el string en minúscula.
3. `.upper()` coloca todo el string en mayúscula.
4. `.strip()` elimina los espacios entre el inicio y final.

---

# Clase #4

## Tipos de datos

Para trabajar con la programación es importante conocer sobre los tipos de
datos. Entre los tipos de datos tenemos:

1. **String** = `str`: Son cadenas de caracteres.

2. **Integer** = `int`: Son los números sin decimal.

3. **Float** = `float`: Son los números decimales.

4. **Boolean** = `bool`: Son el valor `True` o `False` para controlar la
lógica y el flujo de un programa.

### Anotación científica

Sirve para escribir números muy grandes o muy pequeños de manera compacta.
Para realizar anotaciones científicas en Python, se hace de la siguiente
manera:

1. `1e6 = 1000000`
2. `1e-6 = 0.000001`

**Nota**: Los números con anotación científica se escriben en tipo `float`.

---

# Clase #4

## Print y sus usos

`print` es una herramienta poderosa e importante, ya que al final del día la
vamos a usar a lo largo de nuestro código casi todo el tiempo.

`print` es la puerta de entrada a la comunicación de tus programas con el
mundo exterior.

**Métodos básicos de print**:

1. Usándolo para imprimir en consola mensajes, variables, funciones, datos,
etc.

2. **Concatenar**:

    Existen varias maneras para hacerlo:

   - **Uso del operador `+`**:

        Cuando usas este operador, une las cosas tal cual están sin agregar
        espacios. Recuerda agregar espacios para que quede realmente bien.

3. **Uso de la coma**:

        Con la coma puedes unir cosas para que se impriman en la misma 
        expresión de `print`. Cuando la usas, te coloca un espacio por
        defecto.

4. **Uso de `sep`**:

    sintaxis: `sep="value"`

    Con este método puedes controlar la separación de los valores con las
    comas. De esta manera tendrás impreso las variables separadas con el
    carácter que te guste.

5. **Uso del `end`**:

    sintaxis: `end="value"`

    Cuando `print` termina de imprimir algo, siempre al final agrega un salto
    de línea, para que otra cosa se imprima en la siguiente línea en la parte
    de abajo.

    Para cambiar eso podemos usar `end` y con eso controlar el comportamiento
    al final cuando algo se termine de imprimir.

6. **Uso de formatos con `f-strings`**:

    Podemos imprimir varias cosas y de distintas maneras, atención a los
    siguientes métodos:

   - **Most Common**:

        `f'{} {}'`

        Con este método puedes imprimir texto y variable/funciones, en los
        corchetes colocas las variables/funciones. El texto lo puedes poner
        antes o después de un corchete.

---

# Clase #5

