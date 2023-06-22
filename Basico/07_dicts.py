# Diccionarios

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre": "Patri", "Apellido": "Vadillo", "Edad": 28, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre": "Patri", 
    "Apellido": "Vadillo", 
    "Edad": 28, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1: 1.63
    }

print(my_dict)

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

print(my_dict["Lenguajes"]) # va a mostrar los valores de la propiedad Lenguajes
print(my_dict["Nombre"])

my_dict["Nombre"] = "Maria"
print(my_dict["Nombre"]) # se reemplaza el valor

my_dict["Calle"] = "Plutarco"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Patri" in my_dict) # False
print("Nombre" in my_dict) # True. Estamos buscando por clave, no por valor

print(my_dict.items()) # muestra la clave y el valor
print(my_dict.keys()) # muestra la clave
print(my_dict.values()) # muestra el valor
print(my_dict.fromkeys(("Nombre", 1)))

my_new_dict = dict.fromkeys(("Nombre", 1)) # se puede hacer con dict para hacer el diccionario vacío
print(my_new_dict) # se crea un diccionario sin valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # se ha quedado solamente con las claves, sin los datos
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Patri", "Vadillo"))
print(my_new_dict)

print(dict.fromkeys(list(my_new_dict.keys())))