#solicitar 3 productos

print("="*28)
print("Ingrese el primer producto")

producto_1=(input())
print("Ingrese el precio")

precio_1=float(input())

print("="*28)
print("Ingrese el segundo producto")

producto_2=(input())
print("Ingrese el precio")

precio_2=float(input())

print("="*28)

print("Ingrese el tercer producto")

producto_3=(input())
print("Ingrese el precio")

precio_3=float(input())

print("="*28)

sub_total=(precio_1 + precio_2 + precio_3)

IVA= sub_total * 0.15

total_a_pagar= sub_total + IVA

print(f"Subtotal: {sub_total:.0f}")
print("IVA", "15%")
print(f"Total a pagar: {total_a_pagar:.2f}")
print("="*28)
