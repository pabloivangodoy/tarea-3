def determinante_3x3(matriz):
    # Extraer los elementos de la matriz para facilitar la lectura
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    # Calcular el determinante usando la fórmula
    determinante = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    
    return determinante

# Solicitar al usuario que ingrese los elementos de la matriz 3x3
matriz = []
for i in range(3):
    fila = list(map(float, input(f"Ingrese los 3 números de la fila {i+1}, separados por espacios: ").split()))
    matriz.append(fila)

# Calcular y mostrar el determinante
det = determinante_3x3(matriz)
print(f"El determinante de la matriz es: {det}")
