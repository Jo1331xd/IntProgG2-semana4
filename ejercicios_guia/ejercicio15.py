#Salario empleado por hora

nombre=(input("Dime tus nombres: "))
apellido=(input("Dime tus apellidos: " ))

salario_fijo=float(input("Ingrese su salario por cada hora: $"))
horas=float(input("Ingrese el total de horas trabajadas: "))

descuento_renta= 0.05

print("-"*35)

nombre_del_trabajador=(f"{nombre} {apellido}")
salario_por_hora= salario_fijo * horas

descuento= salario_por_hora * descuento_renta
salario_a_pagar= salario_por_hora - descuento

print(nombre_del_trabajador)
print(f"Su sueldo bruto es de: $ {salario_por_hora:.2f}")
print(f"Su descuento de renta es de: $ {descuento:.2f}")
print(f"Su salario a pagar será de: ${salario_a_pagar:.2f}")
