# Exercise 6
# Read the cost of a meal ordered at a restaurant from the user.
# Then compute the tax and tip for the meal.
# Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax).
# The output from your program should include the tax amount, the tip amount, 
# and the grand total for the meal including both the tax and the tip.
# Format the output so that all of the values are displayed using two decimal places.

tax_rate = .0825
tip = .18
meal_amount = float(input("How much was your meal? "))

tax_amount = meal_amount * tax_rate
tip_amount = meal_amount * tip
grand_total = meal_amount + tax_amount + tip_amount

print("Meal amount: %.2f" % meal_amount)
print("Tax amount: %.2f" % tax_amount)
print("Tip amount: %.2f" % tip_amount)
print("-----------------")
print("Grand total: %.2f" % grand_total)