# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

print("Welcome to Guess the Number!")
name = input("Enter Name: ")
print("Can you guess the number corretcly,", name, "?")

import random

number = random.randint(0,100)

guess_number = int(input("Enter number 0-100: "))

while guess_number != number :
    if guess_number > number :
        print("Greater than. Try again. \n")
        guess_number = int(input("Enter number 0-100: "))
    else:
        guess_number < number
        print("Less than. Try again. \n")
        guess_number = int(input("Enter number 0-100: "))

print("That's right! Now you've figured it out!")

