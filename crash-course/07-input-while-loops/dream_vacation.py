# 7-10

responses = {}

polling_active = True

while polling_active:
    name = input("what is your name? ")
    destination = input("where do you want to travel? ")
    
    responses[name] = destination

    repeat = input("shall someone else respond? (y/n) ")
    if repeat == "n":
        polling_active = False

print("\n-----Poll Results-----")
for name, destination in responses.items():
    print(name + " would like to visit " + destination)