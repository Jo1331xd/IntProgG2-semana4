#algoritmo para calcular la masa 

presion=float(input("Ingrese la presion: "))
volumen=float(input("Ingrese el volumen: "))
temperatura=float(input("Ingrese su temperatura: "))

masa= (presion * volumen) / (0.37 * (temperatura + 460))

print(f"El total de la masa sería {masa:.2f}")