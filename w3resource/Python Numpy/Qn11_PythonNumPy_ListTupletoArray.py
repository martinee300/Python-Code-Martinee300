# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:01:24 2018

@author: dsiow
"""

# =============================================================================
# 11. Write a Python program to convert a list and tuple into arrays. Go to the editor
# List to array:
# [1 2 3 4 5 6 7 8] 
# Tuple to array:
# [[8 4 6] 
# [1 2 3]]
# =============================================================================

import numpy as np

listing = [1, 2, 3, 4, 5, 6, 7, 8]

list_to_array = np.array(listing)

print(list_to_array)

tup = (8, 4, 6, 1, 2, 3)

tup_to_array = np.array(tup).reshape(2,3)

print(tup_to_array)