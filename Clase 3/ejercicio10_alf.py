cesta = input("please type the products you wanna purchase separated by a comma for example: Beef, Onions, Pasta, etc: ")
cesta = cesta.split(", ")
for item in cesta:
    print(item)