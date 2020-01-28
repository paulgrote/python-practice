# guest list

# make a list that includes 3 or more people, then print a message to each person inviting them to dinner.

guests = ['Barack Obama', 'Bernie Sanders', 'Elizabeth Warren', 'Pete Buttigieg']
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[0]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[1]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[2]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[3]))
print('There are {} guests.'.format(len(guests)))

# add print statement stating that one guest can't attend
print('Unfortunately, {} cannot attend.'.format(guests[0]))

# modify the list, replacing the name of the guest who cannot attend with the name of a new person i'm inviting
guests[0] = 'Joe Biden'

# print a second set of invitations for each person who is still on my list
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[0]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[1]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[2]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[3]))
print('There are {} guests.'.format(len(guests)))

# add a print statement informing the guests that i found a bigger dinner table
print('Dear guests. I found a bigger dinner table. I will be inviting more people.')

# use insert() to add one guest to the beginning of the guest list
guests.insert(0, 'Julian Castro')

# use insert() to add one guest to the middle of the guest list
guests.insert(2, 'Kamala Harris')

# use append() to add one guest to the end of the guest list
guests.append('Amy Klobuchar')

# print a new set of invitation messages, one for each person on my guest list
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[0]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[1]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[2]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[3]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[4]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[5]))
print('Hello, {}. You are formally invited to join me for dinner on Saturday, January 4 2020.'.format(guests[6]))
print('There are {} guests.'.format(len(guests)))

# print a new line stating that I can only invite two people to dinner
print('Bad news. The table will not arrive in time. I can only invite two guests.')

# use pop() to remove guests from the list one at a time until only two names remain. each time i pop a name, print a message apologizing to the person
apology = 'I am sorry, {}, but I cannot invite you. Maybe another time.'.format(guests.pop(0))
print(apology)
apology = 'I am sorry, {}, but I cannot invite you. Maybe another time.'.format(guests.pop(0))
print(apology)
apology = 'I am sorry, {}, but I cannot invite you. Maybe another time.'.format(guests.pop(0))
print(apology)
apology = 'I am sorry, {}, but I cannot invite you. Maybe another time.'.format(guests.pop(0))
print(apology)
apology = 'I am sorry, {}, but I cannot invite you. Maybe another time.'.format(guests.pop(0))
print(apology)
print('There are {} guests.'.format(len(guests)))

# print a message to the remaining two guests letting them know they're still invited
print('Hello, {}. You are still invited to join me for dinner on Saturday, January 4 2020.'.format(guests[0]))
print('Hello, {}. You are still invited to join me for dinner on Saturday, January 4 2020.'.format(guests[1]))
print('There are {} guests.'.format(len(guests)))

# use del to remove the last two names from the list. print the list to make sure the list is empty
del guests[0]
del guests[0]
print(guests)
print('There are {} guests.'.format(len(guests)))
