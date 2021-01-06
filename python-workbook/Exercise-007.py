# Exercise 7
# Write a program that reads a positive integer, n, from the user
# and then displays the sum of all of the integers from 1 to n.
# Formula: sum = (n)(n+1)/2

user_num = int(input("Please enter an integer: "))
total = (user_num * (user_num + 1))/2

print("The sum of integers from 1 to %i is %i." % (user_num, total))