# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

#STRIPS

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class State:
    def __init__(self, propositions):
        self.propositions = propositions

def apply_action(state, action):
    new_state = State(state.propositions.copy())
    new_state.propositions.difference_update(action.effects)
    new_state.propositions.update(action.preconditions)
    return new_state

def is_goal_state(state, goal):
    return goal.issubset(state.propositions)

def strips(initial_state, goal_state, actions):
    plan = []
    while not is_goal_state(initial_state, goal_state):
        applicable_actions = [action for action in actions if action.preconditions.issubset(initial_state.propositions)]
        if not applicable_actions:
            return None  # No se puede alcanzar el objetivo
        action = applicable_actions[0]  # Tomar la primera acción aplicable
        plan.append(action)
        initial_state = apply_action(initial_state, action)
    return plan

# Definir las acciones del problema
action1 = Action("Mover(A, B)", {"En(A)", "Conectado(A, B)"}, {"En(B)", "¬En(A)"})
action2 = Action("Cargar(A, B)", {"En(A)", "En(B)", "En(Vacia)"}, {"En(A:En(Vacia)", "¬En(A)"})
actions = [action1, action2]

# Definir el estado inicial y el estado objetivo
initial_state = State({"En(A)", "En(Vacia)", "Conectado(A, B)"})
goal_state = State({"En(B)", "¬En(A)"})

# Resolver el problema usando STRIPS
plan = strips(initial_state, goal_state, actions)

if plan:
    print("Plan encontrado:")
    for action in plan:
        print(f"- {action.name}")
else:
    print("No se puede encontrar un plan para alcanzar el objetivo.")


#ADL

pip install pddlpy

from pddlpy import DomainProblem

# Definir el dominio
domain_pddl = """
(define (domain transporte)
  (:requirements :strips)
  (:predicates
    (en_origen ?x - objeto)
    (en_destino ?x - objeto)
    (en_camion ?x - objeto)
    (libre_camion)
    (objeto ?x)
  )
  (:action cargar
    :parameters (?o - objeto ?c - objeto)
    :precondition (and (en_origen ?o) (en_camion ?c) (libre_camion))
    :effect (and (en_camion ?o) (not (en_origen ?o)) (not (libre_camion)))
  )
  (:action descargar
    :parameters (?o - objeto ?c - objeto)
    :precondition (and (en_camion ?o) (en_destino ?c) (not (libre_camion)))
    :effect (and (en_destino ?o) (not (en_camion ?o)) (libre_camion))
  )
)
"""

# Definir el problema
problem_pddl = """
(define (problem transporte-problema)
  (:domain transporte)
  (:objects
    objeto-a objeto-b objeto-c - objeto
    camion-1 camion-2 - objeto
  )
  (:init
    (en_origen objeto-a)
    (en_origen objeto-b)
    (en_origen objeto-c)
    (en_destino objeto-a)
    (en_destino objeto-b)
    (en_destino objeto-c)
    (en_camion camion-1)
    (libre_camion)
  )
  (:goal (and (en_destino objeto-a) (en_destino objeto-b) (en_destino objeto-c)))
)
"""

# Crear un objeto de problema
p = DomainProblem(domain_pddl, problem_pddl)

# Resolver el problema utilizando el planificador
solution = p.horizon_search()

# Mostrar el plan encontrado
if solution:
    print("Plan encontrado:")
    for act in solution:
        print(act)
else:
    print("No se encontró un plan.")
