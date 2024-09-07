def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar al usuario los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular y mostrar el MCD
mcd = calcular_mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es: {mcd}")
