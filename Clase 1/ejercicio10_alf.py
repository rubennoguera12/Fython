peso_payaso = 112
peso_muneca = 75
orden_payaso = int(input("introduzca el numero de payasos que vendio este mes: "))
orden_muneca = int(input("introduzca el numero de munecas que vendio este mes: "))
orden_kg = (orden_muneca*peso_muneca + peso_payaso*orden_payaso)/1000
print(f"el peso del paquete que sera enviado sera de {round(orden_kg,2)}kgs")