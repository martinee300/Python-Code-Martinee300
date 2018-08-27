# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:38:24 2018

@author: dsiow
"""

# =============================================================================
# 4. Write a Python program to create a null vector of size 10 and update sixth value to 11.Go to the editor 
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
# Update sixth value to 11 
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
# =============================================================================

import numpy as np

array = np.zeros((10))

array[6] = 11
