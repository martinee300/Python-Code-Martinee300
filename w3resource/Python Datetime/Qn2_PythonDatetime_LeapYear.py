# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:48:47 2018

@author: dsiow
"""

# =============================================================================
# 2. Write a Python program to determine whether a given year is a leap year
# =============================================================================

input_year = int(input("Type in the year: "))

if input_year%4 == 0:
    if input_year%100 == 0:
        if input_year%400 == 0:
            print("The year %d is a leap year" %(input_year))
        else:
            print("The year %d is NOT a leap year" %(input_year))
    else:
        print("The year %d is a leap year" %(input_year))
else:
    print("The year %d is NOT a leap year" %(input_year))
            