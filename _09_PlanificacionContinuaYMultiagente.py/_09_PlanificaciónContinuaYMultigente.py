# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install scipy

import numpy as np
from scipy.optimize import minimize

# Función de costo para minimizar la distancia al objetivo
def costo(x, *args):
    objetivo = args[0]
    return np.linalg.norm(x - objetivo)

# Función para realizar la planificación de movimiento
def planificacion_movimiento(inicial, objetivo, limites):
    resultado = minimize(costo, inicial, args=(objetivo,), bounds=limites)
    if resultado.success:
        return resultado.x
    else:
        return None

# Puntos de inicio y objetivo
inicial = np.array([1.0, 1.0])
objetivo = np.array([9.0, 9.0])

# Límites del espacio de movimiento
limites = ((0, 10), (0, 10))

# Realizar la planificación de movimiento
nuevo_punto = planificacion_movimiento(inicial, objetivo, limites)

if nuevo_punto is not None:
    print(f"Punto de inicio: {inicial}")
    print(f"Punto de objetivo: {objetivo}")
    print(f"Punto planificado: {nuevo_punto}")
else:
    print("No se pudo encontrar una solución.")
