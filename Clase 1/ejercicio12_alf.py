precio_fresco = 3.49
descuento_viejo = 0.6
precio_descuento = precio_fresco*descuento_viejo
vendido_viejo = int(input("introduzca la cantidad de panes viejos que vendio hoy: "))
vendido_fresco = int(input("introduzca la cantidad de panes frescos que vendio hoy: "))
total_viejo = precio_descuento*vendido_viejo
total_fresco = precio_fresco*vendido_fresco
total_final = total_fresco + total_viejo
print(f"este mes se vendio un total de {round(total_final,2)} euros en pan, de los cuales {round(total_fresco,2)} fueron en pan fresco, y {round(total_viejo,2)} por pan en descuento, habiendo tenido un total de descuentos de {round(((vendido_viejo*precio_fresco)-total_viejo),2)}")