#Calcula la calificacion final de un estudiante con poderaciones:


print("Calificación final de un estudiante :")

print("Ingrese los puntos por tarea: ")
tareas=float(input())

print("Ingrese la nota del examen parcial: ")
examen_p=float(input())

print("Ingrese la nota del examen final")
examen_f=float(input())

tareas_puntos=(tareas * 0.3) 
examen_parcial=(examen_p * 0.3) 
examen_final=(examen_f * 0.4) 

promedio_final= tareas_puntos + examen_parcial + examen_final

print(f"La calificacion final del estudiante es del: {promedio_final:.0f} %")
