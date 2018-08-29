# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:27:27 2018

@author: dsiow
"""

# =============================================================================
# 4. Write a Python program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
# =============================================================================

import pandas as pd

# The lists
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

# Converting lists into series
series1 = pd.Series(list1)
series2 = pd.Series(list2)

# Comparing if each element in both series is equal
print(series1 == series2)

# Comparing if each element in series1 is larger than series2
print(series1 > series2)

# Comparing if each element in series2 is larger than series1
print(series1 < series2)