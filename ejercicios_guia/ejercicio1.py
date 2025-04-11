#persona prestamo

print("Se hace un prestamo de 10,000.00 cordobas en un banco que cobrará una tasa del 27% anual")

prestamo_banco=float(10000)

print("Ingrese cuantos años han pasado desde su prestamo: ")
años_pasados=float(input())

tasa_banco=float(0.27)


total_a_pagar= años_pasados * tasa_banco * prestamo_banco


print(f"Usted tendra que pagar de mas: {total_a_pagar:.0f} cordobas")
