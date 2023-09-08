nombre_completo = input("Ingrese su nombre completo: ")
print(nombre_completo.lower())
print(nombre_completo.upper())
nombres = nombre_completo.split()
primer_nombre = nombres[0]
apellidos = " ".join(nombres[1:])
nombre_formateado = primer_nombre.capitalize() + " " + apellidos.capitalize()
print(nombre_formateado)
