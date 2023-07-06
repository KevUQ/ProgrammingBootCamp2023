# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:46:36 2023

@author: Kevin Offline
"""
from random import *
from math import *
password = ""

# ask for a letter, a word and a number
letter = input("Enter a letter: ")
word = input("Enter a word: ")
number = input("Enter a positive integer: ")

number1 = str((choice([0,1,2,3,4,5]))*int(number))



password = password + word.lower() + number1
print("your new password is: " + password)

if letter[0]=="a" or letter[0]=="A":
    print("password is weak")
elif word=="password" or word=="pass":
    print("password is weak")
elif float(number) < 0:
    print("password is weak")