def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

cadena = input("Ingresa lo que va en la cadena: ")

if palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')