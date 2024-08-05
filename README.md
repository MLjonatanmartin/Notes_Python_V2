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

# Clase #5

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
Las Listas son una colección ordenada de elementos, pueden almacenar 
cualquier tipo de dato, también son mutables lo que significa que se pueden
cambiar, agregar o eliminar elementos después de que haya sido creada. 

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
11. `.sort()`: Ordena la lsita en su lugar. 
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
