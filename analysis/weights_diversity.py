#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 08:03:34 2022

@author: max
"""

import sys
if sys.version_info >= (3,8):
    import pickle
else:
    import pickle5 as pickle
import numpy as np
import os
import matplotlib.pyplot as plt

session = 'TF'

predator_w = []
prey_w = []

wl = os.listdir('../weights/' + session)
wl.sort()

for wf in wl:
    with open('../weights/' + session + '/' + wf, 'rb') as handle:
        w = pickle.load(handle)
        predator_w.append( w['predator'] )
        prey_w.append( w['prey'] )

# %% 

predator = np.array( predator_w )
prey = np.array( prey_w )

# %%

predator_diversity = np.mean( np.std( predator, axis=1 ), axis=1 )
prey_diversity = np.mean( np.std( prey, axis=1 ), axis=1 )

# %% 

plt.clf()
plt.plot( predator_diversity[100:] )
plt.plot( prey_diversity[100:] )
plt.show()