precio = float(input("Ingrese el precio del producto en euros con dos decimales: "))
euros = int(precio)
centimos = int((precio - euros) * 100)
print(f"{euros} euros y {centimos} céntimos")
