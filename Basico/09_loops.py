# Loops / Bucles

# While

my_condition = 0;

while my_condition < 10:
    print(my_condition)
    my_condition += 1
#elif my_condition == 10:
    #print("Mi condición es igual a 10") # no nos acepta el else if, pero si el else
else: # es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break

    print("Mi condición es menor que 20")


print("###")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (28, 1.63, "Patri", "Vadillo", "patrivr95")

for element in my_tuple:
    print(element)

my_set = {"Patri", "vadillo", 28}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Patri", "Apellido": "Vadillo", "Edad": 28}

for element in my_dict:
    print(element) # imprime las claves, no los valores
    if element == "Apellido":
        break
    print("Se ejecuta")
#elif element == 1:
    # print("element vale 1") # no acepta else if
else:
    print("El bucle for para mi diccionario ha finalizado")

for element in list(my_dict.values()):
    print(element) # imprime los valores al convertirlo en una lista

