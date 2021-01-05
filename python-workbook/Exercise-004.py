# Exercise 4
# Create a program that reads the length and width of a farmer's field from the user in feet.
# Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

field_width = float(input("Enter the width of the room (in feet): "))
field_length = float(input("Enter the length of the room (in feet): "))

area = field_width * field_length
acre = area/43560

print("The area of the field is", str(area), "square feet.")
print("The field is", acre, "acres.")
