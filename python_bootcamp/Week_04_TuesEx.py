# Week 4

# Tuesday exercises

# write a for loop that prints out all numbers from 1 to 100 that are divisible by 3
for i in range(1,100):
	remainder = i%3
	if remainder == 0:
		print(i)
	continue
	
# ask user for string input, and write a for loop that will output the vowels within it

user_word = input("Type a word: ")

print("Here are the vowels: ")

for letter in user_word:
	
	vowels = ["a", "e", "i", "o", "u"]

	for vowel in vowels:
		if letter == vowel:
			print(letter)
		
		continue
	continue
