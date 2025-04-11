#Hospital presupuesto

presupuesto=float(input("Ingrese el presupuesto del hospital: $ "))

urgencias_porcentaje= presupuesto * 0.37
pediatria_porcentaje= presupuesto * 0.42
traumotologia_porcentaje= presupuesto * 0.21

print(f"Se utilizara esta parte del dinero: $ {urgencias_porcentaje:.2f} en Urgencias")
print(f"Se utilizara esta parte del dinero: $ {pediatria_porcentaje:.2f} en Pediatría")
print(f"Se utilizara esta parte del dinero: $ {traumotologia_porcentaje:.2f} en Traumotología")
