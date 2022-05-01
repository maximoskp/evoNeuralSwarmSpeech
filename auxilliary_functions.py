#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 07:32:10 2022

@author: max
"""

import numpy as np

def limit_xy(x, y, m):
    v = np.sqrt( x**2 + y**2 )
    if v != 0:
        n = min(v,m)/v
    else:
        n = 0
    return n*x , n*y
# end limit_xy
