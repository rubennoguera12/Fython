nombre = int(input("escriba su nombre: "))
if type(nombre) is str:
    print(f"Tu nombre es {nombre}")
else:
    print("por favor recuerde introducir un texto")

#Preguntar como hacer para crear un input en el que pueda dar error si introduzco un numero 
# en este caso, tengo que mi programa siempre dara tu nombre es + nombre porque input por default es un string, entonces cada valor que meta asi sea numero sera considerado string
