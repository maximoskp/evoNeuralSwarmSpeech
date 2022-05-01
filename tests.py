#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:20:09 2022

@author: max
"""

import World
import Agent
import Evolution

# initialize constants and environment
constants = World.Constants()
environment = World.Environment( constants )

evoConst =  Evolution.Constants()

# initialize some predators and prey
a = []
b = []
for i in range(constants.total_predator_agents):
    a.append( Agent.PredatorAgent( constants=constants, environment=environment ) )
for i in range(constants.total_prey_agents):
    b.append( Agent.PreyAgent( constants=constants, environment=environment ) )

# append agents in environment
environment.set_predator_agents(a)
environment.set_prey_agents(b)

total_generations_number = 1000
current_generation = 0
while current_generation < evoConst.total_generations_number:
    while len(environment.predator_agents) > evoConst.minPopulationSize and len(environment.prey_agents) > evoConst.minPopulationSize:
        environment.update()
    environment.evolve()
    current_generation += 1