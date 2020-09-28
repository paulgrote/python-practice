# 8-6

def city_country(city,country):
    city_full_name = "{}, {}".format(city,country).title()

    return city_full_name

city = city_country('austin', 'texas')
print(city)
city = city_country('new orleans', 'louisiana')
print(city)
city = city_country('dayton', 'ohio')
print(city)