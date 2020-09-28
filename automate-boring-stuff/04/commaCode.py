# Comma Code
# Given a list, write a function that takes a list value as an argument
# and return a string with all the items separated by a comma and space, 
# with and inserted before the last item.

my_list = ['Lagavulin', 
	'Bruichladdich', 
	'Dalwhinnie', 
	'Oban', 
	'Kilkerran', 
	'Ben Nevis',
	'Deanston']

def theScotches(scotches):
	new_list = [scotch + ', ' for scotch in scotches]
	new_list[-1] = new_list[-1].rstrip(", ")
	new_list[-1] = "and " + new_list[-1] + "."

	new_string = "".join(new_list)

	print(new_string)

theScotches(my_list)
