# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:03:18 2018

@author: dsiow
"""

# =============================================================================
# 7. Write a Python program to an array converted to a float type. Go to the editor 
# Sample output:
# Original array 
# [1, 2, 3, 4] 
# Array converted to a float type: 
# [ 1. 2. 3. 4.] 
# =============================================================================

import numpy as np


orig_array = np.array([1,2,3,4])

# np.asfarray returns an array converted to a float type.
conv_array = np.asfarray(orig_array)

# Alternatively, this can be done in one step:
orig_array = np.array([1,2,3,4], dtype = float)
