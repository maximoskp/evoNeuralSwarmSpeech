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
                'food_depletion': 0.1,
                'food_radius': 1.0,
                'food_replenishment': 70
            },
            'predator': {
                'velocity_limit': 7.5,
                'acceleration_limit': 0.75,
                'perception_radius': 100.0,
                'food_level': 100.0,
                'food_depletion': 1.0,
                'food_radius': 30.0,
                'food_replenishment': 70
            },
            'prey': {
                'velocity_limit': 5.0,
                'acceleration_limit': 0.5,
                'perception_radius': 100.0,
                'food_level': 1.0,
                'food_depletion': 1.0,
                'food_radius': 0.0,
                'food_replenishment': 70
            }
        }
    # end make_agent_constants
    
    def make_world_constants(self):
        self.world_width = 700
        self.world_height = 700
        self.total_predator_agents = 100
        self.total_prey_agents = 100
    # end make_world_constants
# end Constants

class Environment:
    def __init__(self, constants):
        self.total_iterations = 0
        self.constants = constants
        self.predator_agents = []
        self.prey_agents = []
        self.genetics = Evolution.Genetics()
    # end init
    
    def update(self):
        self.total_iterations += 1
        self.update_agents()
        self.compute_stats()
    # end update
    
    def update_agents(self):
        agents2die = {
            'predator': [],
            'prey': []
        }
        for a in self.prey_agents:
            a.update_friends_and_enemies( friends=self.prey_agents, enemies=self.predator_agents )
            a.move()
        for a in self.predator_agents:
            a.update_friends_and_enemies( friends=self.predator_agents, enemies=self.prey_agents )
            a.move()
            a2d = a.update_food()
            agents2die['predator'].extend( a2d['predator'] )
            agents2die['prey'].extend( a2d['prey'] )
        # kill agents
        for a in agents2die['predator']:
            self.predator_agents.remove( a )
        for a in agents2die['prey']:
            self.prey_agents.remove( a )
    # end update_agents
    
    def evolve(self):
        self.prey_agents = self.genetics.evolve_population(self.prey_agents, self.constants.total_prey_agents)
        # restore food levels
        for p in self.predator_agents:
            p.restore_food_level()
        self.predator_agents = self.genetics.evolve_population(self.predator_agents, self.constants.total_predator_agents)
    # end evolve
    
    def set_predator_agents(self, agents):
        self.predator_agents = agents
    # end set_predator_agents
    
    def set_prey_agents(self, agents):
        self.prey_agents = agents
    # end set_prey_agents
    
    def compute_stats(self):
        self.predator_food_levels = np.zeros( len( self.predator_agents ) )
        for i, p in enumerate(self.predator_agents):
            self.predator_food_levels[i] = p.food_level
        self.mean_predator_food_level = np.mean( self.predator_food_levels )
        self.median_predator_food_level = np.median( self.predator_food_levels )
        self.std_predator_food_level = np.std( self.predator_food_levels )
        self.max_predator_food_level = np.max( self.predator_food_levels )
        self.min_predator_food_level = np.min( self.predator_food_levels )
# end Environment