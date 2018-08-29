# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:16:58 2018

@author: dsiow
"""

# =============================================================================
# 2. Write a Python program to convert a Panda module Series to Python list and it's type.
# =============================================================================

import pandas as pd

series = pd.Series([1,2,3,4,5])
print(type(series))

listing = series.tolist()
print(type(listing))
