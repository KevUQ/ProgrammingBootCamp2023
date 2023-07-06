# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:06:57 2023

@author: Kevin Offline
"""

def my_little_program(): #functions are defined with def
    
    print("")
    x_str = input("Give me a number:")
    x = int(x_str)
    y_str = input("Give me another number:")
    y = int(y_str)
    print("")
    
    print(bool(x==y))
    
my_little_program()
