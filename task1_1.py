# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:44:04 2023

@author: Kevin Offline
"""

def my_little_program(): #functions are defined with def
    x_str = input("Give me a number:")
    x = int(x_str)
    y_str = input("Give me another number:")
    y = int(y_str)
    result = x + y
    print("The sum of", x, "and", y, "is", result)
    
    
my_little_program()