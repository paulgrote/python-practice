# Exercise 1: 
# Create a program that displays your name and complete mailing address.
# The address should be printed in the format that is normally used in the area where you live.
# Your program does not need to read any input from the user.

name = "Paul Grote"
street_address = "7308 Wolverine St."
city = "Austin"
state = "TX"
zip_code = "78757"

# solution 1: one print statement per line
print(name)
print(street_address)
print(city + ", " + state + " " + zip_code)

#solution 2: concatenation
print(name + "\n" + street_address + "\n" + city + ", " + state + " " + zip_code)

# solution 3: injecting string using format()
print("{}\n{}\n{}, {} {}".format(name, street_address, city, state, zip_code))
