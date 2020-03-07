# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:20:25 2020

@author: snetkova
"""
while True:
    a = input('1st day:\n')
    b = input('checkpoint:\n')
    if not (a.isdigit() and b.isdigit()):
        continue
    i = 1
    dist = int(a)
    while dist < int(b):
        dist = dist * 1.1
        i +=1
    print(f'You\'ve got the result on the {i}th day')
    break