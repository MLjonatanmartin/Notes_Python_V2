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
largo del código se les puede cambiar de valor, se puede reasignar un nuevo valor.

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

# Clase #5

## Print y sus usos

`print` es una herramienta poderosa e importante, ya que al final del día la
vamos a usar a lo largo de nuestro código casi todo el tiempo.

`print` es la puerta de entrada a la comunicación de tus programas con el
mundo exterior.

**Métodos básicos de print**:

1. Su uso más común es para imprimir en consola mensajes, variables, funciones,
datos, etc.

2. **Concatenar**:

    Existen varias maneras para hacerlo:

   - **Uso del operador `+`**:

        Cuando usas este operador, une las cosas tal cual están sin agregar
        espacios. Recuerda agregar espacios para que quede realmente bien.

3. **Uso de la coma `,`**:

    Con la coma puedes unir cosas para que se impriman en la misma expresión
    de `print`. Cuando la usas, te coloca un espacio por defecto.

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

6. **Uso de formatos con `strings`**:

    Podemos imprimir varias cosas y de distintas maneras, atención a los
    siguientes métodos:

    - **Most Common**:

        `f'{} {}'`

        Con este método puedes imprimir texto y variable/funciones, en los
        corchetes colocas las variables/funciones. El texto lo puedes poner
        antes o después de un corchete.

    - **Uso de Formato con `format`**:

        `.format(value1, value2)`

        Con el método `format` es otra manera para insertar valores en 
        cadenas de texto. En los corchetes `{}` usandolos como marcadores 
        de posición, se pueden pasar los valores que uno quiera poner. Por 
        ejemplo:

        ```python
        color = 'azul'
        color_2 = 'verdes'
        print('el cielo es {} y las hojas de los árboles son {}.'.format(azul, color_2))
        ```

        Resultado:

        `el cielo es azul y las hojas de los árboles con verdes.`

7. **Impresión con formato específico**

    Podemos controlar como se imprimen el formato de los números en `python`.
    En este ejemplo, vamos a redondear el número PI a solo dos décimales, 
    para ello usamos `:.2f`que redondea a dos digitos. 

    ```python
    num = 3.14159
    print('Valor: {:2.f}'.format(num))
    ```

    Resultado

    `Valor: 3.14`

8. **Salto de Línea** 

    Para poder hacer los saltos del línea usamos `\n`. Por ejemplo, si 
    hacemos `print('Colores\nMuchos Colores') vamos a tener:

    ```python
    Colores
    Muchos Cholores
    ```

9. **Caracteres Especiales**

    Si necesitamos colocar comillas dobles dentro de comillas simples usamos
    secuencias de escape `\` para que el interprete de python no se confunda.
    Por ejemplo:

    `print('Ella se llama \"Sofia\"')`

    Resultado

    `Ella se llama "Sofia"`

    Con la secuencia de escape `\` podemos usar caracteres especiales evitando
    errores en la sintaxis y podemos imprimir bien lo que necesitamos. 
---

# Clase #6

## Operaciones Matemáticas en `Python`:

Para poder realizar operaciones matemáticas en `python` debemos tener en 
cuenta las reglas de la aritmética, para poder realizar operaciones en el 
orden establecido ya que `python` sigue estas mismas reglas y si no las 
conocemos nuestras operaciones no darán resultados erroneos. 

Para resumirlo, se usa el acrónimo __PENDAS__ que es: parentesis, exponentes,
multiplicación, división, suma y resta. En este mismo orden `python` realiza
las operaciones matemáticas de izquierda a derecha. 

Para realizar operaciones matemáticas usamos los siguientes operadores:

1. **Suma**:

    Con el operador `+` podemos realizar suma. 

2. **Resta**:

    Con el operador `-` podemos realizar resta.

3. **Multiplicación**:
    Con el operador `*` podemos realizar multiplicación.

4. **Potenciación**:
    
    Con el operador `**` podemos realizar potenciación.

5. **División**:
    
    Con el operador `/` podemos realizar divisiones.

6. **División Entera**:
    
    Con el operador `//` podemos realizar divisiones enteras.

    Divisiones enteras quiere decir que tendremos la división sin decimales.

7. **Módulo de la División**:

    Con el operador `%` podemos sacar el módulo de una división.

    El Módulo de una división es el resultado del número sobrante de una
    división, por ejemplo, si dividimos 12 entre 5 nos sobra 2, ese el 
    módulo. 

**NOTA**

No podemos dividir entre cero `0` porque nos da el error: `ZeroDivisionError`

### Shortcuts - Atajos:

Podemos realizar operaciones sencillas de números con una sitaxis corta, 
para hacerlo colocamos la variable luego el operador de la operación, 
seguimos con un  signo igual y por último el número de la operación. 
Por ejemplo:

```python
num = 7
num *= 2
```

Resultado

`14`
    
Con esto nos ahorramos tiempo y no repetimos tanto código. 

## Comparaciones Matemáticas con `Python`:

También podemos realizar operaciones Booleanas con nuestros números en
`python` para poder hacerlo lo hacemos con los siguientes operadores lógicos:

1. **Mayor que** :

    Con el operador `>` podemos ver si un número es mayor a otro.

2. **Menor que**:

    Con el operador `<` podemos ver si un número es menor a otro.

3. **Mayor o igual que**:

    Con el operador `>=` podemos ver si un número es mayor o igual a otro.

4. **Menor o igual que**:

    Con el operador `<=` podemos ver si un número es menor o igual a otro.

5. **Es igual a**:

    Con el operador `==` podemos ver si número es igual a otro.

6. **No es igual a**:

    Con el operador `!=` podemos ver si número no es igual a otro. 

---

# Clase #7 

## Operaciones de Entrada y Salida en Consola

Cuando trabajamos con proyectos que necesitamos datos entrada y de salida 
en la consola usamos la función incorporada de `input()`, con esta función
podemos solicitar datos que un usuario puede ingresar.

**Cosas Importantes de `input()`**:

1. Con `input()` siempre ingresamos los datos a través de la consola. 
2. Para poder ver que hemos ingresado tenemos que usar `print()`.
3. Todo dato ingresado a través de `input()` lo retorna como `string`. 

## Casting - Convertir a Otros Tipos de Datos:

Podemos usar funciones incorporadas para transformar los tipos de datos de 
datos con los siguientes métodos:

1. `int()`: Convierte un valor a un número entero.
2. `float()`: Convierte un valor a un número de punto flotante (decimal).
3. `str()`: Convierte un valor a una cadena de texto. 
4. `boo()`: Convierte un calor a booleano. 

**NOTA**

1. Error al usar _Casting_:
    
    Si hacemos Casting con `input()` de una vez y no le pasamos el tipo de 
    dato correcto puede generar error. Por ejemplo, podemos tener:

    `int(ipunt())`

    y si no le pasamos un valor númerico no dará un error de:

    `ValueError`

---

# Clase #8

## Arrays (Lista) - Introducción General 

Las Listas son una estructura de datos más útilizada y flexible en Python.
Las Listas son una colección ordenada de elementos (indexada), pueden
almacenar cualquier tipo de dato, también son mutables lo que significa 
que se pueden cambiar, agregar o eliminar elementos después de que haya sido
creada. 

**Sintaxis**

Para crear una lista usa los corchetes cuadrados `[]` y sepera los elementos
por comas `,`. Los `string` deben de ir entre comillas simples `''` o 
dobles `""`. Por ejemplo:

```python

numbers = [1, 2, 3, 4, 'cinco']

```

Por otro lado también puedes tener una lista dentro de otra lista o una 
lista que su conjuto de datos sean otras listas. Por ejemplo:

```python

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Métodos Más Comunes de las Listas:

Los métodos que más se usan con lista son:

1. `len()`: Para ver el tamaño total de una lista. 
2. `.append()`: Para agregar un nuevo valor al final de la lista. 
3. `.insert(i, x)`: Agrega un elemento `x`en la posición `i`. 
4. `.index(x)`: Devuelve el índice de la primera aparición del valor `x`. 
5. `max()`: Encuentra el valor más grande.
6. `min()`: Encuentra el valor más pequeño. 
7. `.extend(iterable)`: Extiende la lista agregando elementos de un iterable. 
8. `.remove(x)`: Elimina la primera aparición del valor `x`. 
9. `.pop(i)`: Elimina y devuelve el elemento de la posición `i`. Si no se 
    especifica `i`, elimina y devuelvel el último elemento. 
10. `.count(x)`: Devuelve el número de veces que `x` aparece en la lista. 
11. `.sort()`: Ordena la lista en su lugar. 
12. `.reverse()`: Invierte los elementos de la lista en su lugar. 

## Operaciones de Slicing con Listas

El slicing permite obtener sub-listas a partir de una lista existente, 
utilizando la notnación `[inicio:fin:paso]`. Por ejemplo:

```python

numeros = [1, 2, 3, 4, 6, 7, 8]

sub_lista = numers[1:5] # Elementos desde el índice 1 hasta el 4

sub_lista_con_paso = numeros[::2] # [1, 3, 6, 8]

invertida = numeros[::-1] # [8, 7, 6, 4, 3, 2, 1]
```

**NOTA**

Puedes usar `del` para eliminar posiciones especifica con el índice de una 
lista, o la puedes eliminar toda. Solo hay que tener en cuenta que `del` 
se utiliza para eliminar objetos y la referencia en memoria,no es método de
las litas como tal, sino una declaración del propio lenguaje. Pero se puede
usar sin problema con las listas. 

---

# Clase #9 

## Modificación copia de una listas

al tener una lista, si copiamos la lista asignando la a una nueva variable
ambas van a apuntar al **MISMO OBJETO** en memoria. Esto significa que lo 
que haga en una de ellas se va a reflejar en la otra.  

Para evitar eso, se crea una lista totalmente independiente con el `[:]`

```python

numbers = [1, 2, 3, 4, 5]
numbers_2 = numbers
```

para poder mirar la referencia en memoria, usa el método `id()` de la 
siguiente manera:

```python
id(numbers)
id(numbers_2)
```

En ese ejemplo, lo que pase en una lista se va a ver reflejado en otra. La
manera correcta de tener dos listas totalmente indenpendiente es:

```python
numbers = [1, 2, 3, 4, 5]
numbers_2 = numbers[:]
```

Con eso nos aseguramos que ambas listas sean diferentes. 

---

# Clase #10

## Listas de más dimensiones y Tuplas

### Matrices y/o Listas Anidadas

Cuando tenemos una lista, podemos tener listas dentro de la lista. Estas
pueden ser matrices, ya que se acomodan listas debajo de otras del mismo
tamaño. También, se pueden tener vectores cuando las úbicamos de esa manera.


Podemos, a su vez, ubicarlas como "columnas" y "filas", las columnas son las
verticales y las filas son las Horizontales.

Con las listas anidadas, son otras listas que están dentro de otra. 

Es importante que las listas dentro de otras listas se separan por comas `,`, 
en caso que no las separemos los valores por comas `,` nos causa un error
de sintaxis. 

Por ejemplo:

```python

# Matris

matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
```

Para poder acceder a esa matris (lista), tenemos que recordar la posición de los
valores en programación. Cada cosa comienza en el valor 0, en este caso 
tenemos una lista con 2 valores:

1. 0 es la sublista de 1, 2 y 3.
2. 1 es la sublista de 4, 5 y 6.
3. 2 es la sublista de 7, 8 y 9. 

y cada valor de cada sublista, se cuenta de la misma manera. Para poder
acceder a un elemento de la lista en especifico usamos los `[]`. Por ejemplo:

```python

# Matris

matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix[0]) # Imprime [1,2,3]
```

Ahora si yo quiero acceder a un valor especifico de esta matrix, puedo 
hacer lo de la siguiente manera:

```python

# Matris

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2][1]) # Imprime 8
```

Con este ejemplo veos que accedemos primero a la última lista, y de ahí hemos
accedido al valor 1, que es el 8. 

### Matris y/o Lista Anidada más compleja

Si tenemos una lista más compleja, como por ejemplo:

```python

numbers = [
    [1,2],
    [3,4],
    [5,6],
    [7,8]
]
```

Como podemos ver, tenemos una lista, con listas, que tienen varios valores,
si queremos acceder a  la lista `[5,6]` lo hacemos de la siguiente manera:

```python

numbers = [
    [[1,2], [3,4]],
    [[5,6], [7,8]]
]

print(numbers[1]) # Imprime [5,6], [7,8]

```

Pero si queremos acceder al valor `5`, lo hacemos de la siguiente manera:

```python

numbers = [
    [[1,2], [3,4]],
    [[5,6], [7,8]]
]

print(numbers[1][0][0]) # Imprime 5
```

## Tuplas

Hay dos formas de declarar tuplas:

1. Con `()`, usa los `()` para declarar.
2. Con `(value,)` de esta manera si necesitas declarar una tupla con un solo
valor. 
3. `numbers = 1,2,3,` Python sobre entiende que eso es una tupla, pero mejor
usar los parentesis para que el código se lea mucho más fácil.

Las tuplas son listas inmutables, no sé pueden ni agregar y ni quitar, ni modificar
algún valor. Pero como cosa curiosa, si tienes una lista dentro de una tupla
si puedes modificar la lista, pero la lista se tiene que conservar su estructura
de los valores reconocidos de la tupla, por ejemplo, si tengo una tupla con una
lista de 2 valores, puedo cambiar esos dos valores pero no puedo ni eliminar
o agregar un nuevo valor ya que choca con la inmutabilidad de una tupla. 

ejemplo de tupla:

```python

names = ('luciano', 'miku', 'vegeta')

print(names[1]) # imprime miku

```

Para acceder a las tuplas, o tuplas aninadadas, es de la misma manera como lo
hemos visto antes. 

---

# Clase #11

## Diccionarios

Los diccionarios son para guardar información, como lo dice su nombre son 
diccionarios, en donde tenemos una palabra clave y su significado o valor. 

Para poder declarar un diccionario lo hacemos con los siguientes corchetes `{}`,
para poder colocar el significado de una clave usamos `:` y para separar cada clave
y valor usamos `,`.

Los diccionarios pueden alvergan mucha información, desde cualquier tipo de dato
hasta funciones, configuración de servidores, listas, tuplas y otros diccionarios. 

Las claves, solo pueden ser de valor inmutable, tales como: String, números y 
tuplas. En cambio que los valores si puedes ser mutables. 

### Métodos de los diccionarios (básicos):

1. `.key()`: Es para obtener las palabras claves de los diccionarios. 
2. `.values()`: Es para obrtener los valores de los diccionarios. 
3. `.items()`: Es para obtener las palabras calves y valor en tuplas de un  
diccionario.
4. `del`: Puedes usarlo para eliminar una clave y valor del diccionario.

### Acceder a un diccionario:

Para acceder a un diccionario, usas los siguientes corchetes `[]` y en medio
colocas la clave del diccionario para poder acceder. Si tienes un string, tienes
que poner las comillas respectivas.

---

# Clase # 12
## Comprehension Lists

Son una manera muy fácil y rápida de construir listas en una sola linea de código, 
lo que te permite que tu código sea mucho corto, eficiente y fácil de leer. 

En su sintaxis, tenemos que va en el siguiente orden:

1. nombre de la variable. 
2. corchetes `[]`.
3. expresión de lo que se quiere hacer. 
4. ciclo `for variable in iterator`.
5. `Condicionales` si lo ves necesario. 

Tal cual que así:

`variable = [expresión for item in iterable if condición]`

Como una cosa curiosa, se escriben de izquierda a derecha y se leen de derecha
a izquierda.

## Beneficios:

1. Crear listas de forma rápida y concisa. 
2. Aplicar transformaciones a los elementos.
3. Filtrar elementos.
4. Aplicar una función a cada elemento de una lista.

## Casos de Uso:

1. Crear lista con los nombres de los archivos que termienn en '.txt' en un
directorio.
2. Crear una matris didimensional. 
3. Muchas más cosas, tengo que investigar. 

---
# Clase #13
## Condicionales y operadores lógicos

Cuando estamos programando, a veces es importante tomar decisiones para que
nuestro código se ejecute si pasa algo, no hacer algo sino pasa nada. 
Por ejemplo, si tenemos un programa que verifica la edad de una persona para 
entrar a un lugar, el progama tiene que evaluar y luego tiene que tomar 
la decisión. 

¿Cómo podemos hacerlo? Podemos hacer todo esto con las Condicionales y la manera
de declarar lo son las siguientes:

1. `if <condición>` con esto nosotros podemos colocar una condición que va 
ser evaluada, si la condición se cumple, se ejecuta el código que está por debajo
del if.

2. `elif <condición>`con este podemos agregar más condiciones a evaluar y pasa
de la misma manera.

3. `else` cuando ya hemos evaluado todas las condiciones y todas son falsas, 
usamos else para que ejecute una última cosa en caso que nada sea verdadero. 

Recordemos que para usar esto, la identación es muy importante, cuando declaramos
una de ellas, se crea una identación, para salir de la indentación solo tenemos
que escribes normal como antes sin ningún espacio. 

También podemos tener `if` anidados dentro de otros sin ningún problema.

## Operadores Lógicos:

Cuando vamos a comparar cosas en las declaracion de `if` estos son los operadores
que podemos usar:

1. `and` evalua si dos cosas son verdaderas, en caso que una sea falsa no se 
ejecuta.
2. `or` evaula si una de las condiciones es verdadera, si una es verdadera se 
ejecuta, si ambas son falsas, no se ejecuta.
3. `not` invierte la condición si es verdadera a falsa, y la falsa la vuelve 
verdadera.

## Operadores aritméticos:

1. `>` mayor que.
2. `<` menor que. 
3. `>=` mayor o igual que.
4. `<=` menor o igual que.
5. `==` igual que.
6. `!=` diferente que.

## Consideraciones

Usa por favor los `()` para agrupar declaraciones y que el código sea mucho más
facil de leer, por otro lado, que usando los `()` le dices al interprete de python
con que prioridad quieres que evalue las expresiones. Ya que python, primero evalua
los `()` y luego lo demás, y si usted pone una expresión sin parentesis, python
va a evular las cosas de acuerdo a su nivel de prioridad y puede que su código 
tenga errores. 

