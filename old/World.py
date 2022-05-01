#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 08:00:26 2022

@author: max
"""

import numpy as np
import Evolution

class Constants:
    def __init__(self):
        self.make_agent_constants()
        self.make_world_constants()
    # end init
    
    def make_agent_constants(self):
        self.agent_constants = {
            'generic': {
                'velocity_limit': 1.0,
                'acceleration_limit': 1.0,
                'perception_radius': 11.0,
                'food_level': 1.0,
                'food_depletion': 1.0,
                'food_radius': 1.0,
                'reproduction_radius': 1.0
            },
            'predator': {
                'velocity_limit': 2.0,
                'acceleration_limit': 2.0,
                'perception_radius': 10.0,
                'food_level': 2.0,
                'food_depletion': 2.0,
                'food_radius': 5.0,
                'reproduction_radius': 5.0
            },
            'prey': {
                'velocity_limit': 3.0,
                'acceleration_limit': 3.0,
                'perception_radius': 15.0,
                'food_level': 2.0,
                'food_depletion': 2.0,
                'food_radius': 15.0,
                'reproduction_radius': 7.5
            }
        }
    # end make_agent_constants
    
    def make_world_constants(self):
        self.world_width = 700
        self.world_height = 700
        self.initial_food_available = 100
        self.food_dispersion = 100
        self.food_replenishment_iterations = 10
        self.total_predator_agents = 100
        self.total_prey_agents = 100
    # end make_world_constants
# end Constants

class Environment:
    def __init__(self, constants):
        self.total_iterations = 0
        self.constants = constants
        self.make_initial_food()
        self.predator_agents = []
        self.prey_agents = []
        self.genetics = Evolution.Genetics()
    # end init
    
    def make_initial_food(self):
        self.food_positions = []
        x = np.random.normal( self.constants.world_width/2, self.constants.food_dispersion , self.constants.initial_food_available )
        y = np.random.normal( self.constants.world_height/2, self.constants.food_dispersion , self.constants.initial_food_available )
        for i in range(x.size):
            self.food_positions.append( np.array([ x[i], y[i] ]) )
    # end make_initial_food
    
    def update(self):
        self.total_iterations += 1
        self.update_food()
        self.update_agents()
    # end update
    
    def update_food(self):
        if self.total_iterations % self.constants.food_replenishment_iterations == 0:
            x = np.random.normal( self.constants.world_width/2, self.constants.food_dispersion )
            y = np.random.normal( self.constants.world_height/2, self.constants.food_dispersion )
            self.food_positions.append( np.array([ x, y ]) )
    # end update_food
    
    def update_agents(self):
        for a in self.prey_agents:
            a.update_friends_and_enemies( friends=self.prey_agents, enemies=self.predator_agents )
            a.update_food_intake()
        for a in self.predator_agents:
            a.update_friends_and_enemies( friends=self.predator_agents, enemies=self.prey_agents )
    # end update_agents
    
    def evolve(self):
        self.prey_agents = self.genetics.evolve_population(self.prey_agents, self.constants.total_prey_agents)
        self.predator_agents = self.genetics.evolve_population(self.predator_agents, self.constants.total_predator_agents)
    # end evolve
    
    def set_predator_agents(self, agents):
        self.predator_agents = agents
    # end set_predator_agents
    
    def set_prey_agents(self, agents):
        self.prey_agents = agents
    # end set_prey_agents
# end Environment