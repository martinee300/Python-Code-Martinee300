# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:30:23 2018

@author: dsiow
"""

# =============================================================================
# 8. Write a Python program to create a 2d array with 1 on the border and 0 inside. 
# Expected Output:
# Original array: 
# [[ 1. 1. 1. 1. 1.] 
# [ 1. 1. 1. 1. 1.] 
# [ 1. 1. 1. 1. 1.] 
# [ 1. 1. 1. 1. 1.] 
# [ 1. 1. 1. 1. 1.]] 
# 1 on the border and 0 inside in the array 
# [[ 1. 1. 1. 1. 1.] 
# [ 1. 0. 0. 0. 1.] 
# [ 1. 0. 0. 0. 1.] 
# [ 1. 0. 0. 0. 1.] 
# [ 1. 1. 1. 1. 1.]]
# =============================================================================

import numpy as np

one_array = np.ones((5,5))
print(one_array)

# Subsetting selects the 2nd row to the 2nd last row (1: -1), and 2nd column to the 2nd last column (1: -1)
one_array[1:-1, 1:-1] = 0
print(one_array)