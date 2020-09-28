# 6-7
pets = [
    {'name':'Stella','age':14, 'color':'white and brown'},
    {'name':'Dusty','age':14, 'color':'brown and white'},
    {'name':'Belle','age':10, 'color':'brown'},
    {'name':'Tucker','age':16, 'color':'white'},
]

for pet in pets:
    print('\n')
    print('Pet: {}. \n\tAge: {} \n\tColor: {}'
    .format(pet['name'], pet['age'], pet['color']))
    