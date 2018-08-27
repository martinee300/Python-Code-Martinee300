# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:29:42 2018

@author: dsiow
"""

# =============================================================================
# 3. Write a Python program to display the current date and time.
# Sample Output : 
# Current date and time : 
# 2014-07-05 14:34:14
# =============================================================================

import datetime

now = datetime.datetime.now()

# date.strftime(format) returns a string representing the date, controlled by an explicit format string. Format codes referring to hours, minutes or seconds will see 0 values.

# E.g. This only prints the year, month and date
print(now.strftime("%Y-%m-%d"))

# E.g. This prints the year, month, date, hour(24h format), minute, second
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# E.g. Alternatively, this prints the year, month, date, hour(24h format), minute, second using %T
print(now.strftime("%Y-%m-%d %T"))