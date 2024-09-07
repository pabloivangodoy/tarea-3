def inversa(cadena):
    return cadena [::-1]

cadena = input("Ingrese lo que quiere que se invierta: ")

cadena_invertida = inversa(cadena)
print(f"La cadena inversa es: {cadena_invertida}")