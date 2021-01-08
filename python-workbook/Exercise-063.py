# Exercise 63:
# Create a program that computes the average of a set of values entered by the user.
# The user will enter 0 as a sentinel value to indicate that no further values will be provided.
# Display an appropriate error message if the first value entered by the user is 0.

x = int(input("Enter an integer (0 to quit): "))
count = 0
total = 0

while x != 0:
    count += 1
    
    total = total + x
    
    x = int(input("Enter an integer (0 to quit): "))

if x == 0:
    print("You can't average 0. Try again.")
else:
    average = total/count
    print("The average is:", average)