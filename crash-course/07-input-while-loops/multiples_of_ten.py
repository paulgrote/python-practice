#7-3

user_number = input("Enter a number, dammit. ")
result = int(user_number) % 10

if result == 0:
    print("You entered a multiple of 10. Good job.")
else:
    print("You did not enter a multiple of 10. I guess that's ok.")