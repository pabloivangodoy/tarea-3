def sumar(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)