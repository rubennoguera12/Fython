numero = int(input("please enter an integer number: "))
while True:
    aux =1
    while aux <= numero:
        if numero % aux == 0 and aux != 1 and aux != numero:
                print("you've chosen a not prime number")
                break
        elif aux<=numero:
            aux+=1
        else:
            print("you've chosen a prime number")
            break

