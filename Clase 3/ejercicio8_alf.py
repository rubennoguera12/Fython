precio = float(input("please enter the price of your product: "))
precio = round(precio,2)
precio = str(precio)
preciolista = precio.split(".")
print(f"El monto total son {preciolista[0]} euros con {preciolista[1]} centimos")