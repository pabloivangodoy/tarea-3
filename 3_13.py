def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4
    # Excepto si es divisible por 100, a menos que también sea divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Solicitar al usuario el año
año = int(input("Ingresa un año: "))

# Determinar si el año es bisiesto
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
