#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:26:22 2022

@author: max
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

for sub_folder in ['l_FF', 'l_FT', 'l_TF', 'l_TT']:
    df = pd.read_csv('../data/' + sub_folder + '/_summary.csv')
    # %% 
    plt.clf()
    plt.plot(df['predators'],'-r', label='predators')
    plt.plot(df['prey'],'-g', label='prey')
    plt.legend(loc='best')
    plt.savefig('figs/best_' + sub_folder + '.png')
    # %% 
    plt.clf()
    plt.plot( df['predators']-df['prey'], '-b' )
    plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ), 'r--')
    plt.savefig('figs/diff_' + sub_folder + '.png')
    # %% 
    y = df['predators']-df['prey']
    plt.clf()
    plt.plot( np.arange( len(df['predators']) )[y>=0], y[y>=0], '.r' )
    plt.plot( np.arange( len(df['predators']) )[y<0], y[y<0], '.g' )
    plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ))
    plt.savefig('figs/wins_' + sub_folder + '.png')