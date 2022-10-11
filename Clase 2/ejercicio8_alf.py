numero = int(input("please write an integer number: "))
aux1 = 1
aux2 = 1
while aux1 <= numero:
        lista = list(range(aux2,0,-2))
        print(*lista)
        aux1+=1
        aux2+=2
    