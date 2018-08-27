# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:39:14 2018

@author: dsiow
"""

# =============================================================================
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# =============================================================================

exam_st_date = (11, 12, 2014)

# %s acts a placeholder for a string while %d acts as a placeholder for a number. 
# Their associated values are passed in via a tuple using the % operator.
print("The examination will start from: %d / %d / %d" %(exam_st_date[0], exam_st_date[1], exam_st_date[2]))
