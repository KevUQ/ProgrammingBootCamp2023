# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:19:30 2023

@author: Kevin Offline
"""

xn = 5
numbers = [xn]



for n in range(30):
   
    if xn % 2 == 0:
        xn //= 2
        numbers = numbers + [xn]
    
    else:
        xn = 3 * xn + 1
        numbers = numbers + [xn]
        
    if xn == 1:
        break

        
print(numbers)