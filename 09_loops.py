#LOOPS

#while

my_condition=0


while my_condition <10:
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("Mi condiciones mayor o igual a 10")
print("LA EJECUCION CONTINUA")




while my_condition < 20:
    my_condition += 1
    if my_condition==15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)
print("LA EJECUCION CONTINUA")


#for
my_list=[35,24,62,52,30,30,17]

for element in my_list:
    print(element)

my_tuple=(35,1.77,"Leo","Oscanoa","osac")
for element in my_tuple:
    print(element)

my_set={"Leo","Oscanoa", 22}
for element in my_set:
    print(element)
    
my_dict={"Nombre":"Leo", "Apellido":"Oscanoa" , "Edad":22 , 1:"Python"}
for element in my_dict:
    print(element)

    if element=="Nombre":
        break
    print("Se ejecuta")

else:
    print("El bucle for por diccionario ha finalizado")
print("la ejecucion continua")


for element in my_dict:
    print(element)

    if element=="Nombre":
        continue
    else:
        print("Se ejecuta")
else:
    print("El bucle for por diccionario ha finalizado")


for contador in range(10):
    if contador % 2 == 0:
        continue  # Salta a la siguiente iteración si el número es par
    print(contador)





