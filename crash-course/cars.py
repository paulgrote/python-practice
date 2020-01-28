# organizing a list

# using sort() to permanently sort alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# using sort() and passing the reverse=True argument to sort reverse alphabetically
cars.sort(reverse=True)
print(cars)

# using sorted() to display a sorted list without changing the original order of items
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the orignal list: ')
print(cars)

print('Here is the sorted list: ')
print(sorted(cars))

print('Here is the orignal list again: ')
print(cars)


# using reverse() to reverse the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# using len() to return the length of a list
print(len(cars))
