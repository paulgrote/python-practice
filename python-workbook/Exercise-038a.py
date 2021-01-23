# Exercise 38:
# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user 
# and then report the appropriate name as part of a meaningful message.
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside this range is entered, 
# then your program should display an appropriate error message.

number_of_sides = int(input("How many sides does the shape have? "))
names = {3:'triangle',
        4:'quadrilateral',
        5:'pentagon',
        6:'hexagon',
        7:'heptagon',
        8:'octagon',
        9:'nonagon',
        10:'decagon'
        }

if number_of_sides < 3 or number_of_sides > 10:
    print('You entered a number outside the parameters of this program.')
else:
    print('A %s has %i sides.' % (names[number_of_sides], number_of_sides))