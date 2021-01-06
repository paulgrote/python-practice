# Exercise 5
# In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit,
# and drink containers holding more than one liter have a $0.25 deposit.

# Write a program that reads the number of containers of each size from the user. 
# Your program should continue by computing and displaying the refund that will be received for returning those containers. 
# Format the output so that it includes a dollar sign and two digits to the right of the decimal point. 

deposit_liter_less = 0.10
deposit_over_liter = 0.25

number_liter_or_less = float(input("How many bottles one liter or less do you have? "))
number_more_than_liter = float(input("How many bottles over one liter do you have? "))

refund_amount = (deposit_over_liter * number_more_than_liter) + (deposit_liter_less * number_liter_or_less)
print("Your refund is $%.2f" % refund_amount)