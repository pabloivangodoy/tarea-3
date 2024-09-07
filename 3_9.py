def segundo_mayor(numeros):
    # Eliminar duplicados y ordenar la lista en orden descendente
    numeros_unicos = list(set(numeros))
    numeros_unicos.sort(reverse=True)
    
    # Verificar si hay al menos dos números únicos en la lista
    if len(numeros_unicos) < 2:
        return "No hay suficientes números distintos en la lista."
    
    # Retornar el segundo número mayor
    return numeros_unicos[1]

# Solicitar al usuario los números
numeros = input("Ingresa una lista de números separados por espacios: ").split()
numeros = [float(num) for num in numeros]  # Convertir a números flotantes

# Encontrar y mostrar el segundo número mayor
resultado = segundo_mayor(numeros)
print(f"El segundo número mayor es: {resultado}")
