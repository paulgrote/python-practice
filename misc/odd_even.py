#Ask the user for a number
number = input("Enter a number: ")

#Calculate even or odd
x = int(number) % 2

#Tell the user whether the number is even or odd
if x == 0:
	print("The number is even.")
else:
	print("The number is odd.")


