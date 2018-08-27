# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:21:49 2018

@author: dsiow
"""

# =============================================================================
# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java 
# Output : java
# =============================================================================

import os

# Split the extension from a pathname. Extension is everything from the last dot to the end, ignoring leading dots.  
# Returns "(root, ext)"; ext may be empty.
name, ext = os.path.splitext('file.txt')

print(ext)
