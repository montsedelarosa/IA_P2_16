# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pddlpy

from pddlpy import DomainProblem, Plan

# Definir el dominio
domain_pddl = """
(define (domain transporte-condicional)
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
(define (problem transporte-condicional-problema)
  (:domain transporte-condicional)
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

# Resolver el problema condicional
plan = Plan(p)

# Verificar si se encontró un plan condicional
if plan.cond_plan():
    print("Plan condicional encontrado:")
    for act in plan.actions:
        print(act)
else:
    print("No se encontró un plan condicional.")
