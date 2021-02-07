# Requests input from the user and appends to a .txt file.

# Asks the user to enter a number. Note: The value is a string.
userInput = input("Enter a number: ")

# Create filename variable and assign a file to it.
filename = 'user_numbers.txt'

# Appends the value of userInput to the file. Note: It does not create a new line when appending the value.
with open(filename, 'a') as f:
	f.write(userInput)
