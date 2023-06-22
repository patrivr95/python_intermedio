# Listas / Array / Arreglo
my_list = list();
my_other_list = [];

print(len(my_list));

my_list = [35, 28, 24, 62, 52, 30, 30, 17];

print(my_list);
print(len(my_list));

my_other_list = [28, 1.63, "Patricia"];

print(my_other_list);

print(type(my_other_list));

print(my_other_list[0]);
# print(my_other_list[4]); # da error porque no existe esa posición
# print(my_other_list[-4]); # da error porque no existe esa posición

print(my_other_list.count(28)); # para ver cuantas veces se repite ese dato en la lista

age, height, name = my_other_list; # tiene que estar en la misma posición que la de los elementos en el array, y necesita todos los elementos
print(height) # 1.63 (my_other_list[1])
print(name) # 'Patricia'(my_other_list[2])

name, height, age = my_other_list[2], my_other_list[1], my_other_list[0]; # esto se podría hacer, pero es muy lioso y sería complicarlo
print(height); 

print(my_list + my_other_list); # hemos concatenado dos listas

#my_list = "Hola Python";
#print(my_list)

my_other_list.append("MoureDev")
print(my_other_list);

my_other_list.insert(0, "Acuario");
print(my_other_list);

my_other_list.remove("Acuario"); # elimina el primer elemento que coincida con lo que le pases
print(my_other_list);

my_other_list[0] = "Piscis";
print(my_other_list);


print(my_list);

print(my_list.pop()); # le puedes pasar el índice del elemento que quieres eliminar del array
print(my_list);

del my_list[2]; # la diferencia con remove, es que le tienes que pasar el índice del elemento
print(my_list);

my_new_list = my_list.copy();

my_new_list.reverse();
print(my_new_list);

my_new_list.sort(); # ordena la lista de menor a mayor
print(my_new_list);

print(my_new_list[1:3])

my_list.clear();
print(my_list);
print(my_new_list)