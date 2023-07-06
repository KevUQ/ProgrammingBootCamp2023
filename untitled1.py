# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:16:37 2023

@author: Kevin Offline
"""

num = 5

# Why does it not print 'Exactly 5' when num = 5?
if num>3 and num<6:
    print("Between 3 and 6")
elif num==5:
    print("Exactly 5")
else:
    print("Something else")