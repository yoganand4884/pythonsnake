# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:12:46 2020

@author: yoganand
"""
n = int (input("Enter a number: "))
for Number in range (1, n):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')