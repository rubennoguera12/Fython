monedas = {"Euro": "€", "Dollar":"$", "Yen": "¥"}
pregunta = input("Introduzca el tipo de moneda de su interes: ")
print(monedas.get(pregunta.title(),"No existe"))
