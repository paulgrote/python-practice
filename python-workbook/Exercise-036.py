# Exercise 36:
# Write a program that implements the following conversion from human years to dog years: 
# first two human years = 10.5 dog years; each additional human year = 4 dog years.
# Ensure that the program works correctly for conversions of less than two human years 
# and for conversions of two or more human years. 
# Display an error message if the user enters a negative number.

human_years = float(input("Enter the number of human years: "))

if human_years < 0:
    print("You messed up. Enter a positive number.")
elif human_years < 2:
    dog_years = human_years * 10.5
    print("Your dog is %f human years old." % dog_years)
elif human_years > 20:
    print("That's an old-ass dog!")
else:
    dog_years = (10.5 * 2)+ (human_years * 4)
    print("Your dog is %f human years old." % dog_years)