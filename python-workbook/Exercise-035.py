# Exercise 35: Even or Odd?
# Write a program that reads an integer from the user.
# Then your program should display a message indicating whether the integer is even or odd.

user_integer = int(input("Please enter an integer: "))

if user_integer%2 == 0:
	print("The number you entered is even.")
else:
	print("The number you entered is odd.")
