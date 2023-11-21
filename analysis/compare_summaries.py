#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:26:22 2022

@author: max
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_TT = pd.read_csv('../data/l_TT/_summary.csv')
df_FT = pd.read_csv('../data/l_FT/_summary.csv')
df_FF = pd.read_csv('../data/l_FF/_summary.csv')
df_TF = pd.read_csv('../data/l_TF/_summary.csv')

# %% stats

TT_wins_ratio = np.mean(df_TT['predators'] > df_TT['prey'])
FT_wins_ratio = np.mean(df_FT['predators'] > df_FT['prey'])
FF_wins_ratio = np.mean(df_FF['predators'] > df_FF['prey'])
TF_wins_ratio = np.mean(df_TF['predators'] > df_TF['prey'])
print('TT wins ratio: ' + str(TT_wins_ratio))
print('FT wins ratio: ' + str(FT_wins_ratio))
print('FF wins ratio: ' + str(FF_wins_ratio))
print('TF wins ratio: ' + str(TF_wins_ratio))

TT_mean_balance = np.mean(df_TT['predators'])/ np.mean(df_TT['prey'])
FT_mean_balance = np.mean(df_FT['predators'])/ np.mean(df_FT['prey'])
FF_mean_balance = np.mean(df_FF['predators'])/ np.mean(df_FF['prey'])
TF_mean_balance = np.mean(df_TF['predators'])/ np.mean(df_TF['prey'])
print('TT mean balance: ' + str(TT_mean_balance))
print('FT mean balance: ' + str(FT_mean_balance))
print('FF mean balance: ' + str(FF_mean_balance))
print('TF mean balance: ' + str(TF_mean_balance))

# %% 
plt.clf()
plt.subplot(2,2,1)
plt.plot(df_TT['predators'],'-r', label='predators')
plt.plot(df_TT['prey'],'-g', label='prey')
plt.legend(loc='best')
plt.title('TT')
plt.subplot(2,2,2)
plt.plot(df_FF['predators'],'-r', label='predators')
plt.plot(df_FF['prey'],'-g', label='prey')
plt.legend(loc='best')
plt.title('FF')
plt.subplot(2,2,3)
plt.plot(df_FT['predators'],'-r', label='predators')
plt.plot(df_FT['prey'],'-g', label='prey')
plt.legend(loc='best')
plt.title('FT')
plt.subplot(2,2,4)
plt.plot(df_TF['predators'],'-r', label='predators')
plt.plot(df_TF['prey'],'-g', label='prey')
plt.legend(loc='best')
plt.title('TF')
plt.savefig('figs/summary.png')

# %% 

# plt.clf()
# plt.plot( df['predators']-df['prey'], '-b' )
# plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ), 'r--')
# plt.show()

# %% 

# y = df['predators']-df['prey']
# plt.clf()
# plt.plot( np.arange( len(df['predators']) )[y>=0], y[y>=0], '.r' )
# plt.plot( np.arange( len(df['predators']) )[y<0], y[y<0], '.g' )
# plt.plot(np.arange( len(df['predators']) ), np.zeros( len(df['predators']) ))
# plt.show()