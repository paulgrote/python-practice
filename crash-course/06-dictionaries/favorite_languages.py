# 6-6
favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"ruby",
    "phil":"python",
}

names = ['alejandro','sean', 'phil', 'jeff']

for name in names:
    if name in favorite_languages:
        print("Thanks for responding to the poll!")
    else:
        print("Please take the poll.")
