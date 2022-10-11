saldo_inicial = float(input("introduzca el saldo inicial de su cuenta bancaria: "))
interes = 0.04
print(f"su saldo inicial del ano 2 sera {round(saldo_inicial*(1+interes),2)}\n a principios del ano 3 sera de {round(saldo_inicial*(1+2*interes),2)}\n a principios del ano 4 sera de {round(saldo_inicial*(1+3*interes),2)}")