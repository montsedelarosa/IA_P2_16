# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

from queue import Queue

# Definir una función para verificar si un estado es objetivo
def es_objetivo(estado):
    return estado == "Objetivo"

# Definir una función para generar sucesores de un estado dado
def generar_sucesores(estado):
    # En este ejemplo, simplemente generamos sucesores agregando un número
    return [estado + 1, estado + 2]

# Definir el estado inicial
estado_inicial = 0

# Crear una cola para la búsqueda en amplitud
cola = Queue()
cola.put(estado_inicial)

# Realizar una búsqueda en amplitud en el espacio de estados
while not cola.empty():
    estado_actual = cola.get()

    if es_objetivo(estado_actual):
        print(f"Se encontró el estado objetivo: {estado_actual}")
        break

    sucesores = generar_sucesores(estado_actual)
    for sucesor in sucesores:
        cola.put(sucesor)
