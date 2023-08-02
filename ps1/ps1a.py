# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:26:15 2023

@author: RS
"""

# Initialize main variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04

# Retrieve user input and convert to floats
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# Calculate down payment value
down_payment = total_cost * portion_down_payment

# Execute while loop to determine number of months until target
number_months = 0 # initialize number of months of savings as 0
while current_savings < down_payment:
    number_months+=1
    current_savings += (portion_saved*annual_salary/12)+(current_savings*r/12)

    
print('Number of months:',number_months)