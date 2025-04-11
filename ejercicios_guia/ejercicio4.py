#solicita nombre, precio de un producto y un porcentaje de descuento. Muestra el
#nombre del producto y precio final luego de aplicar el descuento.

nombre = input("Ingrese el nombre del producto: ")

precio = float(input("Ingrese el precio del producto: "))

print("Ingrese el porcentaje a aplicar")

porcentaje_producto= float(input())


precio_final= precio - (precio * (porcentaje_producto/100))

print(f"El precio final del producto {nombre} es: {precio_final:.2f}")


