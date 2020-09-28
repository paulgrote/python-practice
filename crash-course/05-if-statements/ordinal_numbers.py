# 5-11
# store the numbers 1-9 in a list
numbers = [1,2,3,4,5,6,7,8,9]

# loop through the list
for n in numbers:
    # use an if-elif-else chain to print the proper ordinal ending with each number
    # each result should be on a separate line
    if n == 1:
        print(str(n) + 'st')
    elif n == 2:
        print(str(n) + 'nd')
    elif n == 3:
        print(str(n) + 'rd')
    else:
        print(str(n) + "th")