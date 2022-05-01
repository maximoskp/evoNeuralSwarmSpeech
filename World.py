#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 08:00:26 2022

@author: max
"""

import numpy as np

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
    # end make_world_constants
# end Constants

class Environment:
    def __init__(self, constants):
        self.total_iterations = 0
        self.constants = constants
        self.make_initial_food()
        self.agents = []
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
    # end update
    
    def update_food(self):
        if self.total_iterations % self.constants.food_replenishment_iterations == 0:
            x = np.random.normal( self.constants.world_width/2, self.food_dispersion )
            y = np.random.normal( self.constants.world_height/2, self.food_dispersion )
            self.food_positions.append( np.array([ x, y ]) )
    # end update_food
    
    def append_agents(self, agents):
        for a in agents:
            self.agents.append( a )
    # end append_agents
# end Environment