# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print the first three players
print(players[0:3])

# print the second, third, and fourth players
print(players[1:4])

# omit the first number to start at the beginning of the list
print(players[:4])

# print from third player to end of list
print(players[2:])

# print the last three players on the list
print(players[-3:])

# looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
