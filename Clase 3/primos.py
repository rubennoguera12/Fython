num = int(input("escribe un numero "))
for i in range(2,num):
    if (num%i) == 0:
      print("es primo")
    else:
     print("no es primo")