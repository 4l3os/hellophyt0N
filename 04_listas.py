#Listas

my_list = list()
my_other_list=[]


print(len(my_list))

my_list = [35, 24,62,52,30,30,17]

print(my_list)
print(len(my_list))


my_other_list=[35,1.77,"Leo","Oscanoa"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count("Leo"))
print(my_list.count(30))

age, height, name, surname=my_other_list 
print(name)

name, height, age, surname=my_other_list[2] , my_other_list[1] ,my_other_list[0] ,my_other_list[3] 
print(age)

print(my_list + my_other_list)

my_other_list.append("aleos")
print(my_other_list)

my_other_list.insert(1, "Negro")
print(my_other_list)

my_other_list.remove("Leo")
print(my_other_list)

my_other_list[1]="rojo"
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list) 

print(my_list.pop())

print(my_list.pop(2))

my_pop_element=my_list.pop(2)
print(my_pop_element)

del my_list[0]
print(my_list)

my_new_list=my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.append(21)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)


my_list=["Hola Phyton"]
print(type(my_list))






