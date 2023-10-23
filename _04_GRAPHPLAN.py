# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install graphplan

from graphplan import Action, Problem

# Definir acciones
acciones = [
    Action('Acción1', precondiciones={'A'}),
    Action('Acción2', precondiciones={'B'}),
    Action('Acción3', precondiciones={'A', 'B'}, efectos={'C'}),
    Action('Acción4', precondiciones={'C'}, efectos={'D'}),
]

# Definir un problema
problema = Problem(
    acciones,
    estado_inicial={'A', 'B'},
    estado_objetivo={'D'}
)

# Resolver el problema utilizando GRAPHPLAN
solucion = problema.graphplan()

# Mostrar la solución
if solucion:
    print("Plan encontrado:")
    for nivel, acciones in enumerate(solucion):
        print(f"Nivel {nivel}: {', '.join(acciones)}")
else:
    print("No se encontró un plan.")
