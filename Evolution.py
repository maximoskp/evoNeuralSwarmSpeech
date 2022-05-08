#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:02:37 2022

@author: max
"""

import numpy as np
import Agent

class Constants:
    def __init__(self):
        self.minPopulationSize = 5
        self.total_generations_number = 10000
    # end
# end Constants

class Genetics:
    def __init__(self):
        self.mutation_probability = 0.9
        self.mutation_range = [-1, 1]
    # end init
    
    def evolve_population( self, p , total_new ):
        self.new_population = []
        self.total_new = total_new
        while len(p) + len( self.new_population ) < self.total_new:
            self.apply_evolution_step( p )
        return p + self.new_population
    # end evolve_population
    
    def apply_evolution_step( self, p ):
        # select two individuals
        i1, i2 = np.random.randint( len(p) ), np.random.randint( len(p) )
        # crossover
        new1, new2 = self.crossover( p[i1] , p[i2] )
        # mutation in children
        if np.random.random() <= self.mutation_probability:
            self.mutation(new1)
        if np.random.random() <= self.mutation_probability:
            self.mutation(new2)
        if len(p) + len( self.new_population ) < self.total_new:
            self.new_population.append(new1)
        if len(p) + len( self.new_population ) < self.total_new:
            self.new_population.append(new2)
    # end apply_evolution_step
    
    def crossover( self, p1, p2 ):
        gsize = p1.genome.size
        c1 = np.random.randint( np.floor(0.9*gsize)+1 )
        c2 = np.random.randint( c1, np.floor(gsize)+1 )
        g1 = p1.genome
        g2 = p2.genome
        g1[c1:c2] = p2.genome[c1:c2]
        g2[c1:c2] = p1.genome[c1:c2]
        if p1.category == 'predator':
            new1 = Agent.PredatorAgent( genome=g1, constants=p1.constants, environment=p1.environment )
            new2 = Agent.PredatorAgent( genome=g2, constants=p1.constants, environment=p1.environment )
        elif p1.category == 'prey':
            new1 = Agent.PreyAgent( genome=g1, constants=p1.constants, environment=p1.environment )
            new2 = Agent.PreyAgent( genome=g2, constants=p1.constants, environment=p1.environment )
        else:
            print('unknown agent category in evolution: ', p1.category)
        return new1, new2
    # end crossover
    
    def mutation(self, p):
        gsize = p.genome.size
        i = np.random.randint( gsize )
        p.genome[i] = self.mutation_range[0] + np.random.random()*(self.mutation_range[1]-self.mutation_range[0])
    # end mutation
# end evolution
