# Exercise 1: Mailing Address
# Create a program that displays your name and complete mailing address formatted in the manner that you would usually see it on the outside of an envelope.
# Your program does not need to read any input from the user.

name = "Paul Grote"
street_address = "7308 Wolverine St."
city = "Austin"
state = "TX"
zip_code = "78757"

# syntax 1 - using concatenation to create a string
print(name + "\n" + street_address + "\n" + city + ", " + state + " " + zip_code)

# syntax 2 - using the format() method to create a string
print("{}\n{}\n{}, {} {}".format(name, street_address, city, state, zip_code))
