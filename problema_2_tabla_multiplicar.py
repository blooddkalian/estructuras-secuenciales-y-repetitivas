# Problema 2: Tabla de multiplicar
# Estructura repetitiva for para generar los 10 productos

# Se solicita el número al usuario y se convierte a entero
n = int(input('Ingresa un número entero: '))

print(f'\nTabla de multiplicar del {n}:')

# Ciclo from 1 hasta 10 (inclusive) para generar cada línea
for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')
