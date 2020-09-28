# 7-8

sandwich_orders = ['reuben', 'pastrami', 'chicken salad', 'blt', 'meatball sub']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your {} sandwich.".format(current_sandwich))
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("{}: Done.".format(sandwich))

# 7-9
# using the sandwich orders, make sure the sandwich 'pastrami' appears at least 3 times
sandwich_orders = ['reuben', 'pastrami', 'chicken salad', 'pastrami', 'blt', 'pastrami', 'meatball sub']
finished_sandwiches = []
# print a message stating that the deli has run out of pastrami, then use a while loop to remove all the pastrami subs from the list.
print("The deli is out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("I made your {} sandwich.".format(current_sandwich))
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("{}: Done.".format(sandwich))