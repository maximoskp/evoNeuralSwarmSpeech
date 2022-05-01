#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:20:09 2022

@author: max
"""

import World
import Agent

# initialize constants and environment
constants = World.Constants()
environment = World.Environment( constants )

# initialize some predators and prey
a = []
b = []
for i in range(10):
    a.append( Agent.PredatorAgent( constants=constants ) )
    b.append( Agent.PreyAgent( constants=constants ) )

# append agents in environment
environment.append_agents(a)
environment.append_agents(b)