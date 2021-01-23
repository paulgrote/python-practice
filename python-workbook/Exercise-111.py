# Exercise 111:
# Write a program that reads integers from the user and stores them in a list.
# Use 0 as a sentinel value to mark the end of the input.
# Once all of the values have been read, your program should display them
# (except for the 0) in reverse order, with one value appearing on each line.

the_integers = []

answer = int(input("Please enter an integer, or enter '0' to quit."))

while answer != 0:
    the_integers.append(answer)
    answer = int(input("Please enter an integer, or enter '0' to quit."))

the_integers.reverse()

for i in the_integers:
    print(i)