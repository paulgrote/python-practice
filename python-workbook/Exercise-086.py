# Exercise 86:
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00,
# plus $0.25 for every 140 meters traveled. Write a function that takes the distance traveled
# (in kilometers) as its only parameter and returns the total fare as its only result.
# Write a main program that demonstrates the function. 
# Hint: taxi fares change over time. 
# Use constants to represent the base fare and the variable portion of the fare
# so that the program can be easily updated when the rates increase.

base_fare = 4.00
extra_fare = 0.25

def calculate_fare(distance):
    distance_in_meters = distance * 1000
    total_fare = base_fare + ((distance_in_meters/140) * extra_fare)
    return total_fare

def main():
    print(calculate_fare(100))

main()