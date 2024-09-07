def evaluar_polinomio(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1
    
    # Calcular el valor del polinomio
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** (grado - i))
    
    return resultado

# Solicitar al usuario los coeficientes del polinomio
coeficientes = list(map(float, input("Ingresa los coeficientes del polinomio separados por espacios: ").split()))
x = float(input("Ingresa el valor de x: "))

# Calcular y mostrar el valor del polinomio en x
valor_polinomio = evaluar_polinomio(coeficientes, x)
print(f"El valor del polinomio en x={x} es: {valor_polinomio}")
