# Modulos
# si queremos considerar a estos archivos modulos, tenemos un error: al nombrar los ficheros encabezados con un número, no podemos acceder a ellos
# creamos un archivo nuevo con el nombre aceptado para poder usarlo como módulo

import my_module
# from my_module import sum # si queremos importar una función concreta de un módulo, lo hacemos de esta manera
# se llama a la función de la siguiente forma:
    # sum(1, 4, 7) # ya estoy exportando la función en concreto y no ponemos my_module.sum


my_module.sum(1, 4, 7)
my_module.printValue("hola Python!")

import math      #este modulo pertenece a Python

math.pi
print(math.pi)

print(math.pow(2, 8))


import random # este modulo pertenece a Python

from math import pi as PI_VALUE # se puede renombrar para que sea más fácil localizarlo

print(PI_VALUE)
