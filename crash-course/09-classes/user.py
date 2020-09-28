class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = first_name + last_name
        self.password = 'defaultpassword'
        self.login_attempts = 0

    def describe_user(self):
        print('Your user name is ' + self.user_name + '.')
        print('Your password is ' + self.password + '.')
    
    def greet_user(self):
        print('Hello ' + self.first_name + ' ' + self.last_name)
        
    def increment_login_attempts(self):
        

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Paul', 'Grote')
user2 = User('Evander', 'Holyfield')
user3 = User('Clark', 'Kent')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()