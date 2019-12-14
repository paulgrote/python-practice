from random import randint

# Specify weapons
weapons = ("rock", "paper", "scissors")

# Initialize global variables
game_continue = ""
computer_score = 0
player_score = 0
	
while game_continue != "N":
	
	# Generate opponent weapon
	number = randint(1,3)

	if number == 1:
		computer_weapon = weapons[0]

	elif number == 2:
		computer_weapon = weapons[1]
		
	elif number == 3: 
		computer_weapon = weapons[2]

	# Get player weapon
	player_weapon = input("\nChoose your weapon: {}, {}, or {}? ".format(weapons[0],weapons[1],weapons[2]))
	player_weapon = player_weapon.lower()
	print("{} vs. {}.".format(computer_weapon.title(), player_weapon))

	# Validate user entry
	if player_weapon not in weapons:
		print("You forfeit because you did not enter {}, {}, or {}. \nCheck your spelling and try again.".format(weapons[0],weapons[1],weapons[2]))

	# Game results	
	elif player_weapon == computer_weapon:
		print('DRAW!')
		
	elif player_weapon == weapons[0] and computer_weapon == weapons[2]:
		print('Player wins!')
		player_score += 1

	elif player_weapon == weapons[0] and computer_weapon == weapons[1]:
		print('Computer wins!')
		computer_score += 1
		
	elif player_weapon == weapons[1] and computer_weapon == weapons[0]:
		print('Player wins!')
		player_score += 1
		
	elif player_weapon == weapons[1] and computer_weapon == weapons[2]:
		print('Computer wins!')
		computer_score += 1

	elif player_weapon == weapons[2] and computer_weapon == weapons[1]:
		print('Player wins!')
		player_score += 1
		
	elif player_weapon == weapons[2] and computer_weapon == weapons[0]:
		print('Computer wins!')
		computer_score += 1
	
	# Display scores	
	print("\nComputer:\tPlayer:")
	print("{}\t\t{}\n".format(computer_score, player_score))
	
	# Continue game?
	print("Play again? (Y/N)")
	game_continue = input().strip().upper()

print("\nGood bye.")
