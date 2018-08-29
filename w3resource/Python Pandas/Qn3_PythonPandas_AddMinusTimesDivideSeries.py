# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:23:59 2018

@author: dsiow
"""

# =============================================================================
# 3. Write a Python program to add, subtract, multiple and divide two Pandas Series. Go to the editor 
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
# =============================================================================

import pandas as pd

series1 = pd.Series([1,2,3,4,5])
series2 = pd.Series([2,4,6,8,10])

# Adding two series
print(series1+series2)

# Subtracting two series
print(series1-series2)

# Multiplying two series
print(series1*series2)

# Dividing two series
print(series1/series2)
