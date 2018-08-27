# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:57:19 2018

@author: dsiow
"""

# =============================================================================
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504
# =============================================================================

# Need to import this in order to use pi
from math import pi

radius = float(input("Type in the radius of the circle: "))

area = pi*radius**2
print(area)