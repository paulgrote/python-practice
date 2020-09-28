# 5-10
# check user names

# make a list of 5 or more user names called current_users
current_users = ['Paul', 'Rob', 'Stephanie', 'Cornell', 'Darian']

# make another list of 5 user names called new_users
# make sure one or two names are also in the current_users list
new_users = [ 'JAMES', 'BARBARA', 'STEPHANIE', 'DaRiAn']

# loop through the new_users list to see if the name has already been used
# if it has, print a message that the user will need to select a different user name
# if a user name has not been used, print a message saying the name is available
# make sure your comparison is case insensitive
current_users_lowercase = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lowercase:
        print('"{}" already exists. Please select a different user name.'.format(user))
    else:
        print('"{}" is available.'.format(user))