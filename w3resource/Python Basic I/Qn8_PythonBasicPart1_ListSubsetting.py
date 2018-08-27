# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:28:48 2018

@author: dsiow
"""

# =============================================================================
# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# =============================================================================

color_list = ["Red","Green","White" ,"Black"]

print("The first color in the list is " + color_list[0])
print("The last color in the list is " + color_list[-1])

# Alternatively, using string formatting %s here
print("The first color is %s and the last color is %s" %(color_list[0], color_list[-1]))
