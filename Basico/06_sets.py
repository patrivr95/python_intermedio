# Sets

my_set = set();
my_other_set = {};

print(type(my_set));
print(type(my_other_set)); # inicialmente es un dict

my_other_set = {"Patri", "Vadillo", 28};
print(type(my_other_set));

print(len(my_other_set));

# print(my_other_set[0]) # de esta forma no podemos acceder a los elementos del set. ERROR!!
my_other_set.add("patrivr95")
print(my_other_set); # un set no es una estructura ordenada

my_other_set.add("patrivr95"); # un set no admite repetidos
print(my_other_set);

print("Patri" in my_other_set); # si existe en la variable
print("Patry" in my_other_set); # si existe en la variable. Esta es la forma de realizar búsquedas

my_other_set.remove("Patri")
print(my_other_set);

# my_other_set.clear();
# print(len(my_other_set));

# del my_other_set; # desaparece la variable
# print(my_other_set) 

my_set = {"Patri", "Vadillo", 28}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"Python", "JavaScript", "C#"}

my_new_set = my_set.union(my_other_set);
print(my_new_set.union(my_new_set).union({"Angular"})); # no se pueden duplicar los datos, por lo que aparecerán los mismos elementos. Pero el ultimo union si aparece porque ese lenguaje no se repite en la variable

print(my_new_set.difference(my_set))