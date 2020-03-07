# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:02:04 2020

@author: snetkova
"""
while True:    
    n = input('enter the number:\n')    
    if not n.isdigit():
        continue
    sum = 0
    i = 1
    while i < 4:
        sum += int(n * i)
        i += 1
    print(sum)
    break