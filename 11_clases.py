#clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias="sin alias"):
        self.full_name=f"{name} {surname} ({alias})"
    def walk(self):
        print(f"{self.full_name} esta caminando")    

my_person=Person("leo", "oscanoa")
print(my_person.full_name)
my_person.walk()

my_other_person= Person("Leo", "Oscanoa", "Oso")
print(my_other_person.full_name)
my_other_person.walk()
my_person.full_name= "Ale Ramirez (El loco de los perros)"
print(my_person.full_name)
