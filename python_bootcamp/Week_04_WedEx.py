# Week 4

# Wednesday exercises

# write a while loop that continues to ask for user input and runs until they type 'quit'
user_quit = ""

while user_quit != "quit":
	user_quit = input("Enter a word: ")

# write a for loop within a while loop that will count from 0 to 5, 
# but when it reaches 3, it sets a game_over variable to True and breaks out of the loop

game_over = False
while game_over != True:

	for i in range(6):
		if i < 3:
			print(i)
		else:
			game_over = True
