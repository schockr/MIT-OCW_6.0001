# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:06:29 2023

@author: RS
"""

cube = -15
epsilon = 0.0001
num_guesses = 0
low = 0
high = cube
if cube < 1:
    low = cube
    high = 1
guess = (high+low)/2
while abs(guess**3-cube)>= epsilon:
    if guess**3<cube:
        low = guess
    else:
        high = guess
    guess = (high+low)/2
    num_guesses+=1
print('num_guesses =',num_guesses)
print(guess,'is close to the cube root of',cube)