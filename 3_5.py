def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0 
    suma_total = sum(calificaciones)
    promedio = suma_total / len(calificaciones)
    return promedio

calificaciones = input("Ingresa las calificaciones separadas por espacios: ").split()
calificaciones = [float(calificacion) for calificacion in calificaciones]  # Convertir a números flotantes

promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calificaciones es: {promedio:.2f}")
