# 7-4

prompt = "What is a topping you want on your pizza? \n(Enter quit when you are done entering toppings. "
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print("You added {}".format(topping))