# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:13:08 2020

@author: snetkova
"""
while True:
    n = input('enter the number (>=0):\n')
    if not n.isdigit():
        continue
    l = len(n)
    i = 0
    mx = 0
    while i < l:
        digit = (int(n) // 10**i) % 10
        if digit > mx:
            mx = digit
        else:
            pass
        i +=1
    print('max digit: ', mx)
    break
