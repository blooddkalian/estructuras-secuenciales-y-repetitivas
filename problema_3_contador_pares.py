# Problema 3: Contador de números pares
# Combina estructura repetitiva (for) con selectiva (if)

# El usuario define cuántos números va a ingresar
cantidad = int(input('¿Cuántos números deseas ingresar? '))

contador_pares = 0  # Contador de números pares

# Ciclo que se repite 'cantidad' veces
for i in range(cantidad):
    numero = int(input(f'Ingresa el número {i+1}: '))
    # Si el residuo de dividir entre 2 es 0, es par
    if numero % 2 == 0:
        contador_pares += 1  # Se incrementa el contador

print(f'\nTotal de números pares: {contador_pares}')
