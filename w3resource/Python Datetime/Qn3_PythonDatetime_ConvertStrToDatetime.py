# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:57:53 2018

@author: dsiow
"""

# =============================================================================
# 3. Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM 
# Expected Output : 2014-07-01 14:43:00
# =============================================================================

import datetime as dt

date_string = 'Jan 1 2014 2:43PM'

date_format = '%b %d %Y %I:%M%p'

datetime_obj = dt.datetime.strptime(date_string, date_format)

print(datetime_obj)
