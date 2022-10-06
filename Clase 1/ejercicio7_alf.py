peso_kg = float(input("introduzca su peso en kilogramos (kg): "))
altura_m = float(input("introduzca su altura en metros (m): "))
imc = (peso_kg/(altura_m)**2)
print(f"tu imc es {round(imc,2)}")