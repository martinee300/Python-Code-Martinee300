# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:15:07 2018

@author: dsiow
"""

# =============================================================================
# 12. Write a Python program to append values to the end of an array. Go to the editor
# Expected Output:
# Original array:
# [10, 20, 30] 
# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]
# =============================================================================

import numpy as np

orig_array = np.array([10, 20, 30])


# Using np.append - the values can be a list or a tuple
orig_array = np.append(orig_array, (40, 50, 60, 70, 80, 90))
