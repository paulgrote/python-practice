# Ask user: "What's my favorite food?"
# If user guesses my favorite food, output: "Yep! So amazing!"
# If not, output: "Yuck! That's not it!"
# End with "Thanks for playing!"

favoriteFood = "Enchiladas"

userGuess = input("What's my favorite food? ")

if userGuess == favoriteFood:
	print("Yep! So amazing!")
	
else:
	print("Yuck! That's not it!")
	
print("Thanks for playing!")
