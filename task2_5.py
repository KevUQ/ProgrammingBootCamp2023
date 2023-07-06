# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:04:27 2023

@author: Kevin Offline
"""
# =============================================================================
# from random import *
# 
# for i in range(randint(65,153)):
#     print(i)
# =============================================================================



# PSEUDO CODE  ====================================
# define the smallest value so far
# use some sort of "for" loop to iterate over our number list
    # for each number
        # is this number smaller than the smalles number we've seen so far
        # if yes
            # set this number to be the smallest number
        # otherwise
            # nothing
# =============================================================================

numbers = [170,909,358,189,555,498,84,725,435,772]
smallest_number = numbers[0]
largest_number = numbers[0]

for number in numbers:
    if number < smallest_number:
        smallest_number = number   
       
    if number > largest_number:
        largest_number = number
        
    else:
        pass
print(smallest_number, largest_number)
print(sorted(numbers))









# =============================================================================
# numbers = [170,909,358,189,555,498,84,725,435,772]
# for i in enumerate(str(numbers)):
#     if numbers[i] < numbers[i+1]:
#         print(f'{numbers[i]}')
# =============================================================================

