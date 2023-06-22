### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i + 1 for i in range(15)] ## va a imprimir el rango de 15 posiciones en la lista, del 0 al 14. Tambien si sumamos, el valor de la posicion i cambia
print(my_list)

my_range =  range(8)
print(list(my_range))

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)