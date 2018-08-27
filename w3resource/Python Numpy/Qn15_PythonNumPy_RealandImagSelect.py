# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:43:30 2018

@author: dsiow
"""

# =============================================================================
# 15. Write a Python program to find the real and imaginary parts of an array of complex numbers. Go to the editor
# Expected Output:
# Original array [ 1.00000000+0.j 0.70710678+0.70710678j] 
# Real part of the array: 
# [ 1. 0.70710678] 
# Imaginary part of the array:
# [ 0. 0.70710678] 
# =============================================================================

import numpy as np

list_x = [1.00000000+0.j, 0.70710678+0.70710678j]

array_x = np.array(list_x)

# Use array.real and array.imag to select real and imaginary parts
array_real = array_x.real
array_imaginary = array_x.imag
