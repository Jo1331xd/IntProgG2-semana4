#pulsasiones por cad 10 segundos

edad=float(input("Ingrese la edad de la persona: "))

numero_pulsasiones= (220 - edad) / 10

print(f"Su numero de pulsasiones es de: {numero_pulsasiones:.2f} BPM")