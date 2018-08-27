# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:57:54 2018

@author: dsiow
"""

# =============================================================================
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615
# =============================================================================

n = 5

nn = int(str(n) + str(n))

nnn = int(str(n) + str(n) + str(n))

print(n + nn + nnn)