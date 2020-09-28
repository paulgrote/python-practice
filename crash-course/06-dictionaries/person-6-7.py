# 6-7
people = [
    {'first_name':'Rob', 'last_name':'Grote', 'age':34, 'city':'Austin'},
    {'first_name':'Stephanie', 'last_name':'Grote', 'age':33, 'city':'Austin'},
    {'first_name':'Belle', 'last_name':'Grote', 'age':10, 'city':'Austin'},
]

for person in people:
    print('\n')
    print('Person: {} {}. \n\tAge: {} \n\tCity: {}'
    .format(person['first_name'], person['last_name'], person['age'], person['city']))
    