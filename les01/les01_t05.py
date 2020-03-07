# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:57:51 2020

@author: snetkova
"""
while True:
    earned = input('How much money did you earn?\n')
    spent = input('How much money did you spend?\n')
    if not (earned.isdigit() and spent.isdigit()):
        continue
    rev = int(earned) - int(spent)
    if rev < 0:
        print('Oops! You\'ve lost your money')
    elif rev == 0:
        print('Oops! You\'ve got nothing')    
    else:
        print ('Great! You\'ve got a profit!')   
        perf = rev/int(earned)
        print('Perfomance = ', perf)
        while True:
            employees = input('How much employees do you have?\n')
            if not employees.isdigit():
                continue
            rev_per_empl = rev/int(employees)
            print('Revenue per employee = ', rev_per_empl)
            break
    break