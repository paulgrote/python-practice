class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + ' is a ' + self.cuisine_type + ' restaurant.')

    def restaurant_open(self):
        print(self.restaurant_name + ' is open.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        self.number_served += number

restaurant1 = Restaurant('Via 313', 'pizza')
restaurant2 = Restaurant("Tyson's tacos", 'taco')
restaurant3 = Restaurant('Brewtorium', 'german')
restaurant4 = Restaurant('Easy Tiger', 'bread')

restaurant1.describe_restaurant()
restaurant1.restaurant_open()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print(restaurant4.number_served)
restaurant4.set_number_served(7)
print(restaurant4.number_served)
restaurant4.increment_number_served(40)
print(restaurant4.number_served)
