# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:37:19 2018

@author: dsiow
"""

# =============================================================================
# 1. Write a Python program to get the powers of an array values element-wise. 
# Note: First array elements raised to powers from second array
# Expected Output:
# Original array 
# [0 1 2 3 4 5 6] 
# First array elements raised to powers from second array, element-wise: 
# [ 0 1 8 27 64 125 216]
# =============================================================================

import numpy as np

array = np.array([0, 1, 2, 3, 4, 5, 6])

powers = np.full(7,3)

print(array**powers)
