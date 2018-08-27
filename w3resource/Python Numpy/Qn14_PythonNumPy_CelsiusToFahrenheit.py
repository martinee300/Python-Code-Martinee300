# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:31:11 2018

@author: dsiow
"""

# =============================================================================
# 14. Write a Python program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array. Go to the editor
# Sample Array [0, 12, 45.21 ,34, 99.91]
# Expected Output:
# Values in Fahrenheit degrees:
# [ 0. 12. 45.21 34. 99.91] 
# Values in Centigrade degrees: 
# [-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778] 
# =============================================================================

import numpy as np

list_celsius = [-17.77777778, -11.11111111, 7.33888889, 1.11111111, 37.72777778]

array_celsius = np.array(list_celsius)

array_fahrenheit = (9/5)*array_celsius + 32
