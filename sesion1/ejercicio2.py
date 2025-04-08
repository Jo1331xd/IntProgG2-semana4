cantidad=10
precio= 130 
total= cantidad * precio

def ftexto(texto):
    return f"{texto:>10}"

#Esta está manera de hacerlo
print(f"{ftexto("Cantidad:" )}:{cantidad:>6}")
print(f"{ftexto("Precio: ")}:{precio:>6}")
print(f"{ftexto("Total: ")}:{total:>6}")

#Pero esta está otra tambien

print(f"{"Cantidad:":>10} {precio:>6}")

