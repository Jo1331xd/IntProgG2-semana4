#Nuevo salario empleado

salario_empleado= float(input("Ingrese el salario del empleado: $"))

incremento_salario= float(0.08)

descuento_servivios= float(0.025)

nuevo_salario= salario_empleado * incremento_salario
descuento_salario= salario_empleado * descuento_servivios

total_salario= salario_empleado + nuevo_salario - descuento_salario

print("El nuevo salario del empleado es: $", total_salario)