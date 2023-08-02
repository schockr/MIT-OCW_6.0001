# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:26:15 2023

@author: RS
"""

# Initialize main variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
epsilon = 100

# Retrieve user input and convert to floats
annual_salary = float(input('Enter your annual salary: '))

# Calculate down payment value
down_payment = total_cost * portion_down_payment


num_guesses = 0
low = 0
high = 10000
guess = (high+low)/2
            

while abs(current_savings - down_payment) >= epsilon:
    current_savings = 0
    temp_annual_salary = annual_salary
    savings_rate = guess/10000
    for number_months in range(0,36):
        if number_months%6 == 0 and number_months > 0:
            temp_annual_salary *= (1+semi_annual_raise)
        monthly_salary = temp_annual_salary/12
        current_savings+= monthly_salary*savings_rate+current_savings*r/12
        
    if current_savings < down_payment:
        low = guess
    else:
        high = guess
        
    guess = (low+high)/2
    num_guesses+=1
    if num_guesses>13:
        break
    
# output
if num_guesses > 13:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', savings_rate)
    print('Steps in bisection search:', num_guesses)