# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:02:58 2023

@author: RS
"""
import math
import numpy

x = None
y = None
while True:

    x1 = input('Enter number x: ')
    y1 = input('Enter number y: ')
    try:
        x = int(x1)
        y = int(y1)
        break
    except:
        continue

print('x**y = ',x**y)
print('log(x) = ',numpy.log2(x))