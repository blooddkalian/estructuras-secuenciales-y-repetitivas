# Problema 1: Promedio de calificaciones
# Se usan estructuras repetitivas (for) para leer y sumar calificaciones

suma = 0  # Variable acumuladora inicializada en 0

# Ciclo for que itera 5 veces (una por materia)
for i in range(5):
    calificacion = float(input(f'Ingresa la calificación de la materia {i+1}: '))
    suma += calificacion  # Se acumula cada calificación

# Se calcula el promedio dividiendo la suma entre el número de materias
promedio = suma / 5
print(f'El promedio final es {promedio:.1f}')
