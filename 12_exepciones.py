#excepciones handling:manejo de errores

numberOne=5 
numberTwo=1
numberTwo="1"

if type(numberTwo)==int:
    
    print(numberOne + numberTwo)
else:
    print("no se cumplio")


numberOne=5 
numberTwo=1
numberTwo="1"

#try except 
try:
    print(numberOne + numberTwo)
    print("no error")
except:
    print("error")

#try except else
try:
    print(numberOne + numberTwo)
    print("no error")
except:#se ejecuta si  se produce una excepcion
    print("error")
else:#opcional
    #se ejecuta si no se produce una excepcion
    print("La EJECUCION CONTINUA CORRECTAMENTE")
finally:#opcional
    #se ejecuta siempre
    print("La ejecucion continua")

#excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("no error")
except ValueError:
    print("error valueerror")
except TypeError:
    print("error typeerrror")

#Captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("no error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)








