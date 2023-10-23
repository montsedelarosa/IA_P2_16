# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#Vigilancia de ejecución

import time

# Función que representa una tarea a vigilar
def tarea_a_vigilar():
    for i in range(5):
        print(f"Ejecutando paso {i + 1} de la tarea...")
        time.sleep(1)  # Simula una espera de 1 segundo por paso
    print("Tarea completada")

# Función de vigilancia de ejecución
def vigilancia_ejecucion():
    tarea_iniciada = False
    while True:
        if not tarea_iniciada:
            print("Iniciando la tarea a vigilar...")
            tarea_iniciada = True
            tarea_a_vigilar()  # Iniciar la tarea
        else:
            print("La tarea está en progreso...")
            time.sleep(1)  # Esperar 1 segundo
            estado = "completada" if tarea_completada() else "en progreso"
            print(f"Estado de la tarea: {estado}")

            if tarea_completada():
                break

# Función que simula verificar si la tarea ha sido completada
def tarea_completada():
    # En este ejemplo, asumimos que la tarea se ha completado después de 5 segundos.
    return time.time() - inicio_tiempo >= 5

inicio_tiempo = time.time()
vigilancia_ejecucion()

#Vigilancia de replanificación

import time

# Función que representa una tarea a ejecutar
def tarea():
    for i in range(3):
        print(f"Ejecutando paso {i + 1} de la tarea...")
        time.sleep(1)  # Simula una espera de 1 segundo por paso
    print("Tarea completada")

# Función de vigilancia y replanificación
def vigilancia_replanificacion():
    tarea_iniciada = False
    intentos = 0

    while True:
        if not tarea_iniciada:
            print("Iniciando la tarea...")
            tarea_iniciada = True
            tarea()  # Iniciar la tarea
        else:
            print("La tarea está en progreso...")
            time.sleep(1)  # Esperar 1 segundo
            estado = "completada" if tarea_completada() else "en progreso"
            print(f"Estado de la tarea: {estado}")

            if tarea_completada():
                print("Tarea completada con éxito.")
                break
            else:
                print("¡Se ha detectado un problema!")
                intentos += 1

                if intentos < 3:
                    print(f"Intento {intentos}: Replanificando la tarea...")
                    replanificar_tarea()
                else:
                    print("Se han agotado los intentos. La tarea no se puede completar.")
                    break

# Función que simula verificar si la tarea ha sido completada
def tarea_completada():
    # En este ejemplo, asumimos que la tarea se ha completado después de 3 segundos.
    return time.time() - inicio_tiempo >= 3

# Función de replanificación
def replanificar_tarea():
    print("Realizando una replanificación...")
    # En un caso real, podrías llamar a un sistema de planificación para generar un nuevo plan.

inicio_tiempo = time.time()
vigilancia_replanificacion()
