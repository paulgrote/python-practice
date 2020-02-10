# for loops

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	
# print a message to each magician
for magician in magicians:
	print(magician.title() + ', that was a great trick!')
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	
# statements outside the for loop indentation execute after the for loop completes
print('Thank you, everyone. That was a great magic show!')
