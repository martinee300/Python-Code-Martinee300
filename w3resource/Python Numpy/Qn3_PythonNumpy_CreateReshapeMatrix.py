# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:24:51 2018

@author: dsiow
"""

# =============================================================================
# 3. Create a 3x3 matrix with values ranging from 2 to 10. 
# Expected Output:
# [[ 2 3 4] 
# [ 5 6 7] 
# [ 8 9 10]] 
# =============================================================================

import numpy as np

listing = list(range(2,11))

# Use the reshape method to change it into a 3x3 matrix
array = np.array(listing).reshape(3,3)
