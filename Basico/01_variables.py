
my_string_variable = 'My String variable'; # lo más correcto es definir una variable en formato snake y en minúsculas
print(my_string_variable);

my_int_variable = 45;
print(my_int_variable);

my_int_to_str_variable = str(my_int_variable);
print(my_int_to_str_variable);
print(type(my_int_to_str_variable));

my_bool_variable = True;
print(my_bool_variable);

# Concatenación de variables en un print
 # print(type(print(my_string_variable, ',' , str(my_int_variable), ',' , my_bool_variable))); # 'class NoneType' : python ha petado. 'print' es una función como tal, no un tipo de dato.

print(my_string_variable, ',' , str(my_int_variable), ',' , my_bool_variable);

# Algunas funciones del sistema
print(len(my_string_variable)) # 'len' es una abreviatura de 'length', y cuenta los caracteres de la variable

# Variables en una sola línea
name, surname, alias, edad = "Patri", "Vadillo", "Patri", 28; # he creado tres string por un lado y un entero. No es buena práctica pero simplemente es para saberlo.
print("Me llamo:", name, "Mi apellido es:", surname, "Mi alias es:", alias, "Y tengo: ", edad);
print(type(edad));
print(type(name));

# Inputs
"""
first_name = input('Cual es tu nombre?: ');
age = input('Cual es tu edad?: ');

print(first_name);
print(age);
"""

name = 123;
age = 45;
print(name);
print(age);

# Forzamos el tipo
address : str = "Mi dirección";
address = 32;
print(type(address));