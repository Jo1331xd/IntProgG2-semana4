#rutina de persona en recorrer la misma ruta de siempre

lunes=float(input("¿Cuantos minutos tardaste en correr este lunes?: "))
martes=float(input("¿Cuantos minutos tardaste en correr este martes?: "))
viernes=float(input("¿Cuantos minutos tardaste en correr este viernes?: "))

promedio= lunes + martes + viernes

print(f"Tu tiempo recorrido en la semana es de: {promedio:.2f} minutos")