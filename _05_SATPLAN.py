# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pycosat

import pycosat

# Definir un problema SAT en forma CNF (Forma Normal Conjuntiva)
def problema_satplan():
    # Variables proposicionales
    a = 1
    b = 2

    # Cláusulas CNF
    clausulas = [
        [a],          # Cláusula 1: a
        [-a, b],      # Cláusula 2: no a o b
        [-b]          # Cláusula 3: no b
    ]

    return clausulas

# Resolver el problema SAT utilizando pycosat
clausulas = problema_satplan()
solucion = pycosat.solve(clausulas)

# Mostrar el resultado
if solucion is not None:
    print("Plan encontrado:")
    plan = [variable for variable in solucion if variable > 0]
    for variable in plan:
        print(f"Variable {variable} es verdadera en el plan.")
else:
    print("No se encontró un plan.")
