# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:03:51 2022

@author: ashot
"""

s = input("Input a string")

d=l=0

for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        
        l+=1
    else:
        pass
    
print("Letters", l)
print("Digits", d)