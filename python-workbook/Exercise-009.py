# Exercise 9
# Pretend that you have just opened a new savings account that earns 4 percent interest per year.
# The interest that you earn is paid at the end of the year, 
# and is added to the balance of the savings account.
# Write a program that begins by reading the amount of money deposited into the account from the user.
# Then your program should compute and display the amount in the savings account after 1, 2, 3 years.
# Display each amount so that it is rounded to 2 decimal places. 

interest_rate = 0.04
starting_deposit = float(input("Enter the starting deposit amount: "))

year_1_balance = starting_deposit + starting_deposit * interest_rate
year_2_balance = year_1_balance + year_1_balance * interest_rate
year_3_balance = year_2_balance + year_2_balance * interest_rate

print("Balance after year 1: %.2f" % year_1_balance)
print("Balance after year 2: %.2f" % year_2_balance)
print("Balance after year 3: %.2f" % year_3_balance)