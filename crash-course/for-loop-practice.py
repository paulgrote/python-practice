# use a for loop to print the numbers 1 to 20, inclusive
for i in range(1,21):
	print(i)

# make a list of the numbers from 1 to 1,000,000, then....
millions = []
for million in range(1,1000001):
	millions.append(million)

# use a for loop to print the numbers
#for i in range(0,1000001):
# 	print(millions[i])

# use min() and max() to make sure the list actually starts at one and ends at one million
print(min(millions))
print(max(millions))

# use sum() to add all the numbers
print(sum(millions))

# use the third argument of the range() function to make a list of the odd numbers from 1 to 20
# use a for loop to print each number
odd_numbers = []
for odd in range(1,20,2):
	odd_numbers.append(odd)
print(odd_numbers)

# make a list of the multiples of 3 from 3 to 30. use a for loop to print the numbers in the list
multiples_of_3 = []
for multiple in range(1,11):
	multiples_of_3.append(multiple*3)
for multiple in multiples_of_3:
	print(multiple)

# make a list of the first 10 cubes (the cube of each integer from 1 to 10) and use a for loop to print out the value of each cube
cubes = []
for cube in range(1,11):
	cubes.append(cube**3)
print(min(cubes))
print(max(cubes))
print(cubes)
for cube in cubes:
	print(cube)

# use a list comprehension to generate a list of the first 10 cubes
cubes2 = [cube**3 for cube in range(1,11)]
print(min(cubes2))
print(max(cubes2))
print(cubes2)
for cube in cubes2:
	print(cube)
