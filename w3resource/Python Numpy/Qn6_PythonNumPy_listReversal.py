# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:52:43 2018

@author: dsiow
"""

# =============================================================================
# 6. Write a Python program to reverse an array (first element becomes last).
# Original array: 
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37] 
# Reverse array: 
# [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12] 
# =============================================================================

import numpy as np

listing = list(range(12,38))
listing.reverse()

array = np.array(listing)
