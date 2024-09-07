def calcular_factorial(numero):
    factorial = 1
    while numero > 1:
        factorial *= numero
        numero -= 1
    return factorial

num = int(input("Ingresa un numero para calcular su factorial: "))

if num >= 0:
    resultado = calcular_factorial(num)
    print(f"El factorial de {num} es {resultado}")
else:
    print("Por favor, ingrese un numero no negativo.")