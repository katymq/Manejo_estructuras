# -*- coding: utf-8 -*-
"""Manejo_estructuras_datos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UzpLEYHYMBbzC1XauKwQclhTiBfcxGub

<center> <h1> Estructuras de datos en Python </h1>

![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncB2fp8FCRjubfKXk8Hvl_NA8ycwu2BmHwQ&usqp=CAU)

</center>




Expositor: Katherine Morales

- Linkedin [in/katherine-morales-7194a3108/](https://www.linkedin.com/in/katherine-morales-7194a3108/)

# String Data Type

- Es una secuencia de caracteres 
- Para strings, + significa concatenar
- Cuando un string cintiene números, este es todavía un string
- Podemos convertir números que están en formato string a un número utilizando **int()**
"""

str1 = "Hola"
str2 = ' mundo'

msj = str1 + str2
print(msj)

str3 = '123'
x = str3 + 1

x = int(str3) + 1
print(x)

"""## Leer y transformar

Cuando 'leemos' los datos puede suceder que se lean como strings (es lo que prefiere la máquina.

"""

entrada = input('Ingrese un nombre ')

entrada

entrada.__class__

edad = input('Ingrese su edad: ')

edad

edad + 5

# Solución al problema
# Aqui

"""## Buscando dentro de los strings

- Utilizamos corchetes para acceder a un caracter  []
- El índice debe ser entero
- También puede ser una expresión calculable
"""

nombre =

letra = nombre[]

print(letra)

indice = 
letra2 = nombre[]





"""- Len function"""

ejemplo = 'taller'



"""- Loops con strings

Tarea:
Usando **while** y una variable de iteración, con ayuda de len, se imprima en pantalla el índice y la letra correspondiente

0 t

1 a

2 l

3 l

4 e

5 r



- La variiable de iteración itera a lo largo de la seguencia 
- Ejecuta el cuerpo, el bloque de código
- La variable de iteración se mueve a lo largo de todos los valores en la secuencia
"""







"""Tarea: contar el número de veces que una letra aparece en una frase"""

texto = 'Estamos aprendiendo las estructuras de datos que existen en python y como manejarlas '

"""## Algunos métodos

"""

ejemplo3 = 'Katherine Morales'

ejemplo3.lower()

ejemplo3.upper()

type(ejemplo3)

dir(ejemplo3)

ejemplo3.split()

ejemplo3.replace('Katherine', 'Tania')

ejemplo3.replace('s', 'z')

# find
# lstrip
# rstirp
# strip

# análisis sintáctico y extracción

"""## Extras

"""

ejemplo

'e' in ejemplo

'k' not in ejemplo

ejemplo > ejemplo2

"""- Análisis sintáctico y extracción
- Strings y conjuntos de caracteres

# Listas

Al igual que un string, una lista es una secuencia de valores. En una cadena, los valores son caracteres; en una lista, pueden ser de cualquier tipo. Los valores de una lista se denominan elementos o, a veces, ítems.
"""

lista1 = [1, 2, 3, 5]

lista2 = ['Curso', 'Python', 'Estructuras', 'Datos']

lista3 = [1, [3,5], 3]

lista = []

for k in lista1:
  print(k)

"""Tarea: Crear una lista de  5 nombres e imprimer el mensaje personalizado para cada uno de ellos de Feliz Navidad (Nombre)

Feliz Navidad Pablo!

Feliz Navidad Mariana!
"""

# Code here
nombres = []

"""- Listas son mutables (podemos cambiar un elemento de una lista usando el operador index)

- Strings son inmutables (no podemos cambiar el contenido de un string)

"""



"""El tamaño de una lista - len()"""



"""Acceder a los elementos []"""

lista1



type(lista1)

"""### Métodos de una lista"""

dir(lista1)

lista1

x = []
x = list()
x

x.append(4)
x

x.append(5)

x

x.remove(4)

x

"""- Enlace strings con listas"""

texto

palabras = texto.split()
palabras

texto2 = 'Este es un ejemplo. Para separar. por puntos'
texto2.split('.')

texto3 = 'micorreo@dominio'
texto3.split('@')

lista1 + lista2

lista2*3

"""# Dictionaries

- Key
- Value

-
"""

d1 = dict()
d1['clave1'] = 2
d1['clave2'] = 3
d1['clave3'] = 24
d1

d1['clave1']

d1['clave1'] = 33
d1

"""Necesito guardar la información de cuántas veces se repite cada nombre:

Diego, Tania, Katherine, Juan, Alex, Alejandro, Diego, Juan, Alex, Diego, Tania, Katherine, Juan, Juan, Alex, Alejandro, Alex, Tania, Katherine, Alejandro
"""

# code here

"""Actualizar con la siguiente información:

Tania, Paul, Juan, Paul
"""

# code here

"""Automatizar el proceso"""

informacion = dict()



"""Métodos"""

dir(informacion)

informacion

# Get un valor por defecto si la key no está en el diccionario
informacion.get('Pedrito', 0)

informacion = dict()

nombres = ['Diego','Tania','Katherine','Juan','Alex','Alejandro','Diego','Juan','Alex','Diego','Tania','Katherine','Juan','Juan','Alex','Alejandro','Alex','Tania','Katherine','Alejandro']

for nombre in nombres:
  informacion[nombre] = informacion.get(nombre, 0) + 1
print(informacion)

"""TAREA

Ingrese por pantalla un texto (largo), se busca contar las veces que aparece cada palabra en el texto. Almacenar esto en un diccionario
"""

#code here

print('Comenta si te ha gustado la charla y qué quisieras aprender: ')
comentario = input()



"""Keys and Values"""

informacion.keys()

informacion.values()

informacion.items() # Resultado: tupla

"""## Loops con diccionarios"""

for clave in informacion:
  print(clave, informacion[clave])

for clave, valor in informacion.items():
  print(clave, valor)

"""# Tuplas
Son otro tipo de secuencia, se parecen un poco a las listas PERO son objetos **inmutables**



"""

tupla1 = ('Kathy', 'Juan', 'Pedro')
type(tupla1)

print(tupla1[1])

tupla1[1] = 'Pablo'

(x, y) = (2, 55)
print(y)
print(x)

"""Tuplas y diccionarios"""

x = informacion.items()

x # list of tuples

