# Clases

# los nombres de las clases se escribe en mayúsculas en camelcase

class MyPerson:
    pass 

print(MyPerson())
print(MyPerson)


# esto significa que esta Persona reciba algún parámetro. Es un constructor de clase que no está haciendo nada, por eso le pasamos pass. Qe devuelva None no es necesario ponerlo
# Lo mejor, es que tuviera un archivo donde tuviera a la clase Person, y lo llamaría desde el archivo principal.
# Como ya tenemos datos que pasarle, le quitamos el pass
# El uso del self es obligatorio. Si queremos una clase con constructor, tenemos que pasarselo obligatoriamente, ya que se refiere a la clase que acabamos de crear. Le igualamos self a las propiedades que hemos creado en esa clase.

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name # Propiedad privada, ya no se puede modificar
        self.surname = surname # Propiedad pública
        self.alias = alias # Propiedad pública

    def get_name (self):
        return self.__name # Conseguir la propiedad privada

    def walk (self):
        print(f"{self.name} está caminando")


my_person = Person("Patri", "Vadillo", "patrivr95")
print(f"{my_person.name} {my_person.surname} {my_person.alias}")
my_person.walk() # no le ponemos print a esto porque el método walk de la clase Person ya tiene un print

my_person.name = "Hector"
my_person.surname = "de León"
my_person.alias = "El loco de los perros"
print(f"{my_person.name} {my_person.surname} {my_person.alias}")
my_person.walk()

my_person.name = 65
print(f"{my_person.name}")