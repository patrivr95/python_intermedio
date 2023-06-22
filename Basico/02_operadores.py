# Operadores aritméticos

print(3 + 4);
print(10 // 3); # esto nos va a dar el número entero
print(10 / 3); # esto nos va a dar el número decimal
print(2 ** 3); # exponente


print("Hola" + "Python");
print("Hola " + str(5));
print("Hola" * 5); # se imprime el 'Hola' cinco veces

my_float = 2.5 * 2; # el resultado es un float
print("Hola " * int(my_float)); # lo convertimos en int para poder realizar la operación, ya que con una variable de tipo float no se va a poder realizar

# Operadores comparativos
print(3 == 4); # el resultado es False
print(3 <= 4); # el resultado es True

# Estamos comparando los caracteres de las cadenas de texto por orden alfabético ASCII
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print(len("aaaa") >= len("abaa")) # Cuenta los caracteres (len)
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Operadores lógicos
print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" < "Python")
print(not(3 > 4))