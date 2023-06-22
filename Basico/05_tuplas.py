# Tuplas

# Estas son las dos formas de definir una tupla, que es un conjunto de valores

my_tuple = tuple();
my_other_tuple = ();

my_tuple = (28, 1.63, "Patricia", "Vadillo");
print(type(my_tuple))

my_other_tuple = (35, 60, 24, 28)

print(my_tuple[0]); # llego también a los elementos con el índice

print(my_tuple.count("Patricia"));
print(my_tuple.index(1.63));

# my_tuple[1] = 1.65; # no se puede modificar los valores de la tupla. Las tuplas son inmutables
# print(my_tuple);

my_sum_tuple = my_tuple + my_other_tuple;
print(my_sum_tuple); # se pueden concatenar


print(my_sum_tuple[3:6]);

my_tuple = list(my_tuple);
print(type(my_tuple));

my_tuple[1] = 1.65;
my_tuple.insert(2, "Acuario");
my_tuple = tuple(my_tuple);
print(my_tuple);
print(type(my_tuple));

# del my_tuple; # al hacer el del, hace el borrado del del, es decir, de la variable completa, por lo que al hacer print, da error porque no existe
# print(my_tuple);
# del my_tuple[2] # esto también es un error y tampoco se podría hacer