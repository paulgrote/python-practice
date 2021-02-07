class Restaurant():
    '''
    This is a class that represents a restaurant.
    '''
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name + ' serves ' + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name + ' is open.')

    def number_served(self, 0):


# make an instance of restaurant
restaurant = Restaurant('Via 313', 'pizza')

#print the two attributes individually, then call both methods
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# create three different instances of Restaurant and call describe_restaurant() for each
restaurant1 = Restaurant("Tyson's tacos", 'taco')
restaurant2 = Restaurant('Brewtorium', 'german')
restaurant3 = Restaurant('Easy Tiger', 'bread')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# print the number of customers a restaurant has served, change the number, then print it again

# class aRestaurant():

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(self.restaurant_name + ' is a ' + self.cuisine_type + ' restaurant.')

#     def restaurant_open(self):
#         print(self.restaurant_name + ' is open.')

#     def set_number_served(self, number_served):
#         self.number_served = number_served

#     def increment_number_served(self, number):
#         self.number_served += number

# restaurant1 = Restaurant('Via 313', 'pizza')
# restaurant2 = Restaurant("Tyson's tacos", 'taco')
# restaurant3 = Restaurant('Brewtorium', 'german')
# restaurant4 = Restaurant('Easy Tiger', 'bread')

# restaurant1.describe_restaurant()
# restaurant1.restaurant_open()

# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# print(restaurant4.number_served)
# restaurant4.set_number_served(7)
# print(restaurant4.number_served)
# restaurant4.increment_number_served(40)
# print(restaurant4.number_served)
