# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:49:58 2023

@author: Kevin Offline
"""


# if x_n is even, x_(n+1) = x_n / 2
# otherwise, x(n+1) = 3x_n + 1

# print each x_i for i in [1,30]

xn = 5

for n in range(30):
    print(f"x_{n} is {xn}")
    if xn%2 == 0:
        xn /=2
    else:
        xn=3*xn+1
        
print(f"x_{n} is {xn}")