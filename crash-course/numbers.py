# using the range() function

# generate a series of numbers from 1 to 5
for value in range(1,6):
	print(value)

#create a list of numbers
numbers = list(range(1,6))
print(numbers)

# use the range() function to print the even numbers between 1 and 10
even_numbers = list(range(2,11,2))
print(even_numbers)

# making a list of the first 10 square numbers
squares = []
for value in range(1,11):
	squares.append(value**2)
	
print(squares)

# numeric functions
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
