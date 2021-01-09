# Exercise 110:
# Write a program that reads integers from the user and stores them in a list.
# Your program should continue reading values until the user enters 0.
# Then it should display all of the values entered by the user (except for the 0) in ascending order,
# with one value appearing on each line. 
# Use either the sort() method or the sorted function to sort the list.

user_number = int(input("Enter a number (enter 0 to quit):"))
all_numbers = []

while user_number != 0:
    all_numbers.append(user_number)
    user_number = int(input("Enter a number (enter 0 to quit):"))

all_numbers.sort()

for n in all_numbers:
    print(n)