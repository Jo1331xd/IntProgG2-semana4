#Algoritmo para calcular el porcentaje de varones y mujeres en un aula
print("En un total de 60 alumnos")

print("¿Cuantos varones hay en el salón?: ")
varones_salon=float(input())

print("¿Cuantas mujeres hay en el salón?: ")
mujeres_salon=float(input())

total_salon=float(60)

porcentaje_varones= (varones_salon / total_salon) * 100

porcentaje_mujeres= (mujeres_salon / total_salon) * 100

print(f"Hay un total del: {porcentaje_varones:.0f} % de varones que han llegado al salón")
print(f"Hay un total del: {porcentaje_mujeres:.0f} % de mujeres que han llegado al salón")

porcentaje_no_llegado= 100 - (porcentaje_varones + porcentaje_mujeres)

print(f"Hay un total del: {porcentaje_no_llegado:.0f} % que no han llegado al salón")

