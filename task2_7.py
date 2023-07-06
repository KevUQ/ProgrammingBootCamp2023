# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:25:13 2023

@author: Kevin Offline
"""
from random import *
numbers = [randint(1,1000) for _ in range(100)]
for n in numbers:
    if n > 990:
        print("We must be lucky")
        break
    print(".",end='')
    
    
    
# Write a program that gives the user 5 math questions. 
# If they get anyone wrong they fail and it stops. 
# If they reach all 5 correct they win.

# 