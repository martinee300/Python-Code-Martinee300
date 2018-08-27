# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:09:26 2018

@author: dsiow
"""

# =============================================================================
# Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] 
# One-dimensional numpy array: [ 12.23 13.32 100. 36.32] 
# =============================================================================

import numpy as np

original_list = [12.23, 13.32, 100, 36.32]

# Using np.array to create an array
numpy_array = np.array(original_list)

print(numpy_array)