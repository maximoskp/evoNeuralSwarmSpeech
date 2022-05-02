#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:20:09 2022

@author: max
"""

import World
import Agent
import Evolution
import csv

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

fields=['generation', 'iteration', 'predators', 'prey','food_min','food_mean', 'food_median', 'food_max']
with open('figs/_summary.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
with open('figs/_details.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

while current_generation < evoConst.total_generations_number:
    print('generation: ' + str(current_generation) + '-----------------')
    while len(environment.predator_agents) > evoConst.minPopulationSize and len(environment.prey_agents) > evoConst.minPopulationSize:
        environment.update()
        environment.plot_iteration(generation=current_generation)
        print('predators: ' + str(len(environment.predator_agents)) + ' (' + "{:.2f}".format(environment.min_predator_food_level) + "/{:.2f}".format(environment.mean_predator_food_level)+ "/{:.2f}".format(environment.max_predator_food_level) + ') ' + '\t - prey: ' + str(len(environment.prey_agents)) )
        with open('figs/_details.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ current_generation, environment.total_iterations, len(environment.predator_agents), len(environment.prey_agents), environment.min_predator_food_level, environment.mean_predator_food_level, environment.median_predator_food_level, environment.max_predator_food_level ])
    environment.save_video( generation=current_generation )
    with open('figs/_summary.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([ current_generation, environment.total_iterations, len(environment.predator_agents), len(environment.prey_agents), environment.min_predator_food_level, environment.mean_predator_food_level, environment.median_predator_food_level, environment.max_predator_food_level ])
    environment.evolve()
    current_generation += 1
    with open('figs/_details.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([ 'GENERATION', current_generation, 'GENERATION', current_generation, 'GENERATION', current_generation, 'GENERATION', current_generation ])