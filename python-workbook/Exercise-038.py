# Exercise 38:
# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user 
# and then report the appropriate name as part of a meaningful message.
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside this range is entered, 
# then your program should display an appropriate error message.

number_of_sides = int(input("How many sides does the shape have? "))
name = ''

if number_of_sides == 3:
    name = 'triangle'
elif number_of_sides == 4:
    name = 'quadrilateral'
elif number_of_sides == 5:
    name = 'pentagon'
elif number_of_sides == 6:
    name = 'hexagon'
elif number_of_sides == 7:
    name = 'heptagon'
elif number_of_sides == 8:
    name = 'octagon'
elif number_of_sides == 9:
    name = 'nonagon'
elif number_of_sides == 10:
    name = 'decagon'

if name == '':
    print('You entered a number outside the parameters of this program.')
else:
    print('A %s has %i sides.' % (name, number_of_sides))