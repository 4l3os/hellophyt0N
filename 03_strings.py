#Strings

my_string= "Mi String"
my_other_string= "Mi otro String"

print(len(my_string))
print(len(my_other_string))


print(my_string + "" + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_new_line_string = "\tEste es un string con tabulacion"
print(my_new_line_string)

my_new_line_string = "\tEste es un string con\n escape"
print(my_new_line_string)



#formateo
name, surname, edad="leonardo", "oscanoa", 15
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname,edad))
print("Mi nombre es " + name , surname + " y mi edad es" , edad ) #X NOOO
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")


#Desempaquead de caracteres
language="pythona"
a, b, c ,d ,e ,f,g= language
print(a)
print(e)

#division

language_slice=language[1:3]
print(language_slice) 

language_slice=language[0:3]
print(language_slice) 

language_slice=language[-2]
print(language_slice) 

language_slice=language[1:]
print(language_slice) 

language_slice=language[0:7:3]
print(language_slice) 

#reversa

reversed_language=language[::-1]
print(reversed_language)


#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())










