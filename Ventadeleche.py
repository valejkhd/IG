litros= float(input("Ingrese la cantidad de litros vendidos:  "))
precio= float(input("Ingrese el precio por litro:  "))
galones= litros/3.78541
precio= galones*precio
print("El precio total de la venta de leche es: ", precio)
print("La cantidad de galones vendidos es: ", galones)
