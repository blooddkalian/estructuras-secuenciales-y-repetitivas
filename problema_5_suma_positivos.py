# Problema 5: Suma de números positivos
# Estructura repetitiva while con condición de salida

suma = 0  # Acumulador para la suma de positivos

# Se solicita el primer número antes de entrar al ciclo
numero = int(input('Ingresa un número entero (0 para terminar): '))

# El ciclo continúa mientras el número no sea 0
while numero != 0:
    # Solo se suman los números mayores a 0
    if numero > 0:
        suma += numero
    # Se solicita el siguiente número al final del ciclo
    numero = int(input('Ingresa un número entero (0 para terminar): '))

print(f'\nLa suma de los números positivos es: {suma}')
