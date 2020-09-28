# Write a program that examines three variables - x, y, and z - and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.

x, y, z = 12, 12, 9

if x % 2 == 0:
    if y % 2 == 0 and z % 2 == 0: # none are odd
        print("There are no odd numbers.")
    elif y % 2 != 0 and z % 2 == 0: # y is the only odd
        print("{} is the largest odd number.".format(y))
    elif y % 2 == 0 and z % 2 != 0: # z is the only odd
        print("{} is the largest odd number.".format(z))
    elif y == z: # y and z are equal (and odd)
        print("{} and {} are the same odd number.".format(y,z))
    elif y > z: # y and z are odd, and y is greater
        print("{} is the largest odd number.".format(y))
    elif y < z: # y and z are odd, and z is greater
        print("{} is the largest odd number.".format(z))
elif x % 2 != 0:
    if y % 2 == 0 and z % 2 == 0: # x is the only odd
        print("{} is the largest odd number.".format(x))    
    elif y % 2 != 0 and z % 2 ==0: # x and y are both odd
        if x == y: # x and y are equal (and odd)
            print("{} and {} are the same odd number.".format(x,y))

    elif y % 2 == 0 and z % 2 !=0: # x and z are both odd
        if x == z: # x and z are equal (and odd)
            print("{} and {} are the same odd number".format(x,z))