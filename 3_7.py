def calcular_mediana(numeros):
    numeros.sort()  # Ordenar la lista de números
    n = len(numeros)
    
    # Si la cantidad de números es impar, la mediana es el elemento central
    if n % 2 != 0:
        mediana = numeros[n // 2]
    else:
        # Si la cantidad de números es par, la mediana es el promedio de los dos elementos centrales
        mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    
    return mediana

# Solicitar al usuario los números
numeros = input("Ingresa una lista de números separados por espacios: ").split()
numeros = [float(num) for num in numeros]  # Convertir a números flotantes

# Calcular y mostrar la mediana
mediana = calcular_mediana(numeros)
print(f"La mediana de la lista es: {mediana}")
