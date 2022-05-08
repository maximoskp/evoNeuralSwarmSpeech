#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:26:22 2022

@author: max
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/_summary.csv')

# %% 
plt.clf()
plt.plot(df['predators'],'-r', label='predators')
plt.plot(df['prey'],'-g', label='prey')
plt.legend(loc='best')
plt.show()

# %% 

plt.clf()
plt.plot( df['predators']-df['prey'], '-b' )
plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ), 'r--')
plt.show()

# %% 

y = df['predators']-df['prey']
plt.clf()
plt.plot( np.arange( len(df['predators']) )[y>=0], y[y>=0], '.r' )
plt.plot( np.arange( len(df['predators']) )[y<0], y[y<0], '.g' )
plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ))
plt.show()