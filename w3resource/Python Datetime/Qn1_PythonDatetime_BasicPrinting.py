# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:01:39 2018

@author: dsiow
"""

# =============================================================================
# 1. Write a Python script to display the - Go to the editor
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# =============================================================================

import datetime as dt

# (a) Current date and time
print(dt.datetime.now())

# (b) Current year
print(dt.date.today().strftime("%Y"))

# (c) Month of year
print(dt.date.today().strftime("%m"))

# (d) Week number of the year
print(dt.date.today().strftime("%W"))

# (e) Weekday of the week
print(dt.date.today().strftime("%u"))

# (f) Day of year
print(dt.date.today().strftime("%j"))

# (g) Day of the month
print(dt.date.today().strftime("%d"))

# (h) Day of week
print(dt.date.today().strftime("%A"))
