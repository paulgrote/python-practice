# 7-5

prompt = "Enter your age, and I'll tell you the price of your movie ticket. \n(Enter 'quit' to exit.) "
flag = True
while flag:
    age = input(prompt)
    if age == 'quit':
        flag = False
    elif int(age) < 3:
        print("The ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")