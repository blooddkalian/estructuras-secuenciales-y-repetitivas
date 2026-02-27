# Problema 4: Tarifa de transporte por edad
# Estructura selectiva múltiple (if / elif / else)

# Solicitar la edad del usuario
edad = int(input('Ingresa tu edad: '))

# Validación de entrada: la edad no puede ser negativa
if edad < 0:
    print('Error: la edad ingresada no es válida.')

# Menores de 6 años: tarifa gratuita
elif edad < 6:
    print('Tarifa: Gratis')

# De 6 a 17 años: tarifa reducida
elif edad <= 17:
    print('Tarifa: $10')

# De 18 a 64 años: tarifa general
elif edad <= 64:
    print('Tarifa: $20')

# 65 años o más: tarifa para adulto mayor
else:
    print('Tarifa: $8')
