inversion = float(input("escriba la cantidad de dinero que desea invertir: "))
interes = float(input("escriba la tasa de interes que desea tener (%): "))
interes = interes/100
anos = int(input("escriba la cantidad de anos que su inversion generara intereses: "))
monto_total = (inversion*(1+interes*anos))
print(f"su inversion mas interes sumara un total de {round(monto_total,2)} al final del ano {anos}")