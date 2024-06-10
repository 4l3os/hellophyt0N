#sets

my_set =set()
print(type(my_set))

my_other_set={}
print(type(my_other_set)) #Inicialmente es un dict

my_other_set={"Leo","Oscanoa", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Oscasac")

print(my_other_set)#un set no es una estructura ordenada y no admite repetidos

my_other_set.add("Oscasac")

print(my_other_set)
