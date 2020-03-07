# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:51:50 2020

@author: snetkova
"""
while True: 
    sec = input('Please enter number of seconds: \n')
    if not sec.isdigit():
        continue    
    hh = int(sec) // 3600
    mm = (int(sec) % 3600) // 60
    ss = (int(sec) % 3600) % 60
    print(f'time: {hh:>02}:{mm:>02}:{ss:>02}')
    break