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

print("Leo" in my_other_set)
print("Leoso" in my_other_set)

my_other_set.remove("Leo")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

#del my_other_set no se puede

my_set= {"Leo","Oscanoa",21}
my_list=list(my_set)
print(my_list)

print(my_list[0])

my_other_set={"Kotlin","Swift","Phyton"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set=my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript","C#"}))

print(my_new_set.difference(my_set))






