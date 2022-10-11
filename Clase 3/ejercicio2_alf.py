fullname = input("please write your full name: ")
separados = fullname.split()
for i in range(len(separados)):
    separados[i] = separados[i].lower()
print(*separados)
for i in range(len(separados)):
    separados[i] = separados[i].upper()
print(*separados)
for i in range(len(separados)):
    separados[i] = separados[i].title()
print(*separados)
