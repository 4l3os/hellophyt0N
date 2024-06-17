#funciones

def my_function ():
    print("Esto es una funcion")

my_function ()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5,2)
sum_two_values(4561,451)
sum_two_values("7","5")    
sum_two_values(1.5,1.4)

def sum_two_values_with_return(first_value, second_value):
    my_sum=first_value+second_value
    return my_sum
my_result=sum_two_values_with_return(10,5)
print(my_result)


def print_name(name,surname):
    print(f"{name} {surname}")
print_name("leo", "oscanoa")
print_name(surname="oscanoa", name="leo")


def print_name_with_default(name,surname,alias="sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("leo", "oscanoa", "aleos")
print_name_with_default("leo", "oscanoa")


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola" , "python", "leo")
print_upper_texts("Hola")
