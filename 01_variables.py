#Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_into_to_str_variable=str(my_int_variable)

print(my_into_to_str_variable)
print(type(my_into_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_into_to_str_variable ,my_bool_variable)
print("Este es el valor de : ", my_bool_variable)

#algunos Funciones del sistema

print(len(my_string_variable))

#variables en sola una linea. cuidado con usar
name, surname, alias, age= "Leonardo","Oscanoa","Leo", 35
print("me llamo:", name, surname, "mi edad es:",age,"Y mi alias es", alias)

#Input


#first_name=input(" Cual es tu nombre:  ")

#age=input("Cuantos años tienes:  ")

#print("La gallina se llama",first_name, "Y tiene",age,"años")

#Forzamos el tipo
address: str = "mi direcion"
address: int = 32
print(type(address))



