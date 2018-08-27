# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:49:52 2018

@author: dsiow
"""

# =============================================================================
# 16. Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements. Go to the editor
# Expected Output:
# Size of the array: 3
# Length of one array element in bytes: 8 
# Total bytes consumed by the elements of the array: 24 
# =============================================================================

import numpy as np

# Setting dtype as int will reduce the byte size to 4 bytes per element
# Setting dtype as int will increase the byte size to 8 bytes per element
array = np.array([(1,2,3),(4,5,6),(7,8,9)], dtype = int)

# Returns the number of array elements
size = array.size

# Returns the byte size of each array element
len_bytes = array.itemsize

# Total bytes consumed by the elements of the array.
total_bytes = array.nbytes
