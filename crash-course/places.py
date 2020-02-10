# list of 5 places i want to visit
places = ['vietnam', 'japan', 'czech republic', 'belgium', 'spain']

# print the list in the original order
print(places)

# use sorted() to display the list in alphabetical order
print('Here is the list in alphabetical order: ')
print(sorted(places))
print('Here is the original order again: ')
print(places)
print('Here is the list in reverse alphabetical order: ')
print(sorted(places, reverse=True))
print('Here is the original order again: ')
print(places)

# use reverse() to change the order of the list
print('Here is the list in reverse order: ')
places.reverse()
print(places)
print('Now the list will return to the original order:')
places.reverse()
print(places)

# use sort() to change the order of the list
print('Here is the list in alphabetical order:')
places.sort()
print(places)
print('Here is the list in reverse alphabetical order:')
places.sort(reverse=True)
print(places)
