# Funciones

def my_function (): # esto es suficiente para definir una función
    print("Esto es una función")

# se va a imprimir la función tres veces, ya que la estamos llamando tres veces
my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value): # aunque tipemos los parámetros, podemos concatenar string
    result = first_value + second_value
    print(result)


sum_two_values(3, 5)
sum_two_values("5", "7")
sum_two_values("Hola", ", que tal?") # podemos concatenar texto también
sum_two_values(1.3, 5.2)


def sum_two_values_with_return (first_value, second_value): # aunque tipemos los parámetros, podemos concatenar string
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(56, 35)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Vadillo", name = "Patri")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Patri", "Vadillo")

def print_texts (*texts): #con el asterisco, le puedes pasar infinitos de parámetros
    for text in texts:
        print(text.upper())

print_texts("hola")
print_texts("hola", "Java", "patrivr95")

