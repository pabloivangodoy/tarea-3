from collections import Counter

def calcular_moda(numeros):
    # Contar la frecuencia de cada número en la lista
    contador = Counter(numeros)
    
    # Encontrar la frecuencia máxima
    max_frecuencia = max(contador.values())
    
    # Filtrar los números que tienen la frecuencia máxima
    modas = [num for num, freq in contador.items() if freq == max_frecuencia]
    
    # Si hay más de una moda, se devuelve una lista de modas, de lo contrario, la moda
    if len(modas) > 1:
        return modas
    else:
        return modas[0]

# Solicitar al usuario que ingrese la lista de números
numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))

# Calcular y mostrar la moda
moda = calcular_moda(numeros)
print(f"La moda es: {moda}")
