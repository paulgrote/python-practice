# 6-3, 6-4
rivers = {
    "guadalupe":"texas",
    "nile":"egypt",
    "danube":"austria",
}

for river, country in rivers.items():
    print("The {} river runs through {}.".format(river.title(), country.title()))
