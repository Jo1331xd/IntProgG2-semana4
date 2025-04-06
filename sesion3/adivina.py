#adivinitar un numero
import random

numero_secreto= random.randint(1, 10)

while(True):
    numero_usario= int(input("Dime un numero del 1 al 10: "))

    if(numero_secreto == numero_usario):
        print (f"Felicidades, te ganaste la lotería: {numero_secreto}:")
        break    
    else:print("Sigue intentando...")
    
    if(numero_usario > numero_secreto):
        print("El numero es menor")
    else:
        print("El numero es mayor")