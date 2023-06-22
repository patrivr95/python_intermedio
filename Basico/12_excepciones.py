# Excepciones

numberOne, numberTwo = 5, 1

numberTwo = "1"

#print(numberOne + numberTwo) # Python no suma un int con un str, se da una excepción, y nuestro programa se detiene

#print(5 + "5") # en python tenemos un tipado dinámico: esto significa que si un tipo es un str, podemos pasarlo a un int. 

# podemos poner el else a try except. Si se produce una excepción, el else no se ejecuta.
# finally se ejecuta siempre, haya excepción o no
# el except es obligatorio, en cambio else y finally son opcionales

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")


# Exception por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError: # se ejecuta solo si se produce TypeError. Hay muchos tipos de errores, como ValueError.
    print("Se ha producido TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Captura de la información de la excepción
# la variable error se puede llamar como queramos, pero que sea lógico

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as error: # es una forma de controlar el error, sea lo que sea, capturando la información de la excepción
    print(error)

