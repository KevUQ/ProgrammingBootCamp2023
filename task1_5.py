# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:33:52 2023

@author: Kevin Offline
"""

from math import *

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b**2)-(4*a*c)
print("Determinant is " + str(d))

if d > 0:
    print("2 posible answers, quadratic roots")
    x1=(-b+(sqrt(d)))/(2*a)
    x2=(-b-(sqrt(d)))/(2*a)
     
    print("x1 is " + str(x1))
    print("x2 is " + str(x2))
    
elif d == 0:
    print("1 posible answer, single roots")
    x1=(-b+(sqrt(d)))/(2*a)
    
    print("x is " + str(x1))
   
else:
    print("0 posible answer, not a quadratic")

