# Exercise 37:
# Create a program that reads a letter of the alphabet from the user.
# If the user enters a vowel, then then display a message indicating that the user entered a vowel.
# If the user enters "y", then display a message indicating that y is sometimes a vowel and sometimes a consonant.
# Otherwise, display a message that the letter is a consonant.

the_letter = input("Please enter a letter: ")

if the_letter == "y":
    print("y is sometimes a vowel, sometimes a consonant.")
elif the_letter in "aeiou":
    print("You entered a vowel.")
else:
    print("You entered a consonant.")