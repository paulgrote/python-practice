#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:13:53 2020

@author: paulgrote
"""

# salary variables
annual_salary = 100000 # float(input("Enter the starting salary: "))
portion_saved = 0
semi_annual_raise = .07

# house variables
total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost

# savings variables
current_savings = 0
annual_return = 0.04

# bisection search variables
numGuesses = 0
low = 0
high = 10000
guess = (high + low)/2

month = 0
print("Down payment is: ", down_payment)

# bisection loop
while abs(down_payment-current_savings) >= 100:
    numGuesses += 1

# savings loop
    while current_savings < down_payment:
        month += 1
        monthly_salary = annual_salary/12
        
        monthly_return = current_savings*(annual_return/12)
        current_savings = current_savings + (monthly_salary * portion_saved) + monthly_return
        
        # print("Month", month, ":", current_savings)
        
        if month%6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)

print("Best savings rate: ", month)
print("Steps in bisection search: ", numGuesses)