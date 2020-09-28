# 5-8
# Make a list of five or more user names, including the name 'admin'. 
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user. 
# If the user name is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello, Eric. Thank you for logging in again. 

# 5-9
# Add an if test to make sure the list of users is not empty
# If the list is empty, print the message "We need to find some users!"

user_names = []

if not user_names:
    print("We need to find some users!")
else:
    for name in user_names:
        if name == 'admin':
            print("Hello {}, would you like a status report?".format(name))
        else:
            print("Hello, {}! Thank you for logging in again.".format(name))