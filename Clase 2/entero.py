numero_1 = input("write a number ")
if numero_1.isnumeric():
    numero_1 = int(numero_1)
    if numero_1 % 2 == 0:
        print("your number is even")
    else:
     print("your number is odd")
else:
     print("invalid input")