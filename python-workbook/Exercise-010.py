# Exercise 10
# Create a program that reads two integers, a and b, from the user.
# Compute and display:
# - the sum of a and b
# - the difference when b is subtracted from a
# - the product of a and b
# - the quotient when a is divided by b
# - the remainder when a is divided by b
# - the result of log10a
# - the result of a^b

import math

a = int(input("Enter a number, a: "))
b = int(input("Enter a number, b: "))

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a % b:", a % b)
print("log10a:", math.log10(a))
print("a ** b:", a ** b)
