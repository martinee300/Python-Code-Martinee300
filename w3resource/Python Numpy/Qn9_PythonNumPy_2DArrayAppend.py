# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:45:11 2018

@author: dsiow
"""

# =============================================================================
# 9. Write a Python program to add a border (filled with 0's) around an existing array. Go to the editor
# Expected Output:
# Original array: 
# [[ 1. 1. 1.] 
# [ 1. 1. 1.] 
# [ 1. 1. 1.]] 
# 1 on the border and 0 inside in the array 
# [[ 0. 0. 0. 0. 0.] 
# [ 0. 1. 1. 1. 0.] 
# [ 0. 1. 1. 1. 0.] 
# [ 0. 1. 1. 1. 0.] 
# [ 0. 0. 0. 0. 0.]]
# =============================================================================

import numpy as np

orig_array = np.ones((4,5))

pad_array = np.pad(orig_array, 1, mode = 'constant', constant_values = 0)
print(pad_array)

