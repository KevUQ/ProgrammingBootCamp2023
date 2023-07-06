# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:36:00 2023

@author: Kevin Offline
"""

from random import *
def maths_quiz():
    q = input("enter m for multiplicatoini or a for addition")
    
    if q=="m":
        x = int(100*random())
        y = int(100*random())
        print(f"What is {x} * {y}?")
        correct_ans = x * y
        user_ans = int(input())
        if user_ans == correct_ans:
            print(f"You are right! {x}*{y}={user_ans}")
        else:
            print(f"You are wrong!  {x}*{y} ≠ {user_ans}") #https://www.compart.com/en/unicode/U+2260
    
    
    else:
        x = int(100*random())
        y = int(100*random())
        print(f"What is {x} + {y}?")
        correct_ans = x + y
        user_ans = int(input())
        if user_ans == correct_ans:
            print(f"You are right! {x}+{y}={user_ans}")
        else:
            print(f"You are wrong!  {x}+{y} ≠ {user_ans}") #https://www.compart.com/en/unicode/U+2260
maths_quiz()