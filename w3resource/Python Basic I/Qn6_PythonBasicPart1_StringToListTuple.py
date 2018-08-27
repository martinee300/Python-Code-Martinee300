# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:12:18 2018

@author: dsiow
"""

# =============================================================================
# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output : 
# List : ['3', ' 5', ' 7', ' 23'] 
# Tuple : ('3', ' 5', ' 7', ' 23')
# =============================================================================

seq = input("Input your numbers, separated by commas: ")

seq_list_num = list(map(int, (seq.split(sep = ','))))

seq_tuple_num = tuple(seq_list_num)