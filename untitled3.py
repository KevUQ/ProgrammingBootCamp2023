# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:23:54 2023

@author: Kevin Offline
"""


num = 30

# Why does it not print "Divisible by 5 and 3" if num = 15?
# oreder of logical block
if num%3==0 and num%5==0:
    print("Divisible by 5 and 3.")
    
    
elif num%5==0:
    print("Divisible by 5.")
elif num%3==0:
    print("Divisible by 3.")
else:
    print("Something else.")