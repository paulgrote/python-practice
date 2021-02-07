class User():
    '''
    Creates a user
    '''
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = first_name.lower() + last_name.lower() + '@outlook.com'
        self.password = 'admin123'

    def describe_user(self):
        print('Your credentials:')
        print('User name: ' + self.email_address)
        print('Password: ' + self.password)
    def greet_user(self):
        print('Hello, ' + self.first_name + ' ' + self.last_name)

# create several instances representing different users, and call both methods for each user
user1 = User('Paul', 'Grote')
user2 = User('Evander', 'Holyfield')
user3 = User('Clark', 'Kent')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()