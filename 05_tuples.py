#Tuples

my_tuple=tuple()
my_other_tuple=()

my_tuple=(35, 1.77, "Leo","Oscanoa", "Leo")
my_other_tuple=(35,60,33)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Leo"))
print(my_tuple.index("Oscanoa"))
print(my_tuple.index(35))

#my_tuple[1]=1.80
print(my_tuple + my_other_tuple)

my_sum_tuple=my_tuple+my_other_tuple
print(my_sum_tuple)




