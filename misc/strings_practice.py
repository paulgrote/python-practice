#strings practice
first_name = "paul"
last_name = "grote"
full_name = first_name + " " + last_name
print(full_name.title())
print(full_name.lower())
print(full_name.upper())

message = "Hello " + full_name.title() + "!"
print(message) 

vowels = ["a","e","i","o","u"]

#this doesn't work:
for vowel_number in full_name:
	int(vowels.count(str(full_name)))

vowel_message = "Your name has " + str(vowel_number) + " vowels."
print(vowel_message)
