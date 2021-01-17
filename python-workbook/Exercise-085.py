# Exercise 85:
# Write a function that takes the two shorter sides of a right triangle as its parameters.
# Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function's result.
# Include a main program that reads the lengths of the shorter sides of a right triangle from the user,
# uses your function to compute the length of the hypotenuse, and displays the result.

import math

def compute_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = compute_hypotenuse(a, b)

    print("The hypotenuse is", c)

main()