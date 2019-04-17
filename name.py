#Get date
import datetime
x = datetime.datetime.now()
print("The year is " + str(x.year))

#User input
name = input("Give me your name: ")
age = int(input("Give me your age: "))

#Compute year user turns 100
century = str((x.year - age)+100)

#Display results
print("Your name is " + name + " and you will turn 100 in the year " + century + ".")
