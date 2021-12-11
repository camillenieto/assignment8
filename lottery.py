# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

print("Welcome to the Camille's Lottery!")
print("Remember! enter 0-9 numbers only")

import random

lottery_numbers = []

def lottery() :
    lottery_numbers = []
    for i in range (0,3) :
        number = random.randint (0,9)
        while number in lottery_numbers :
            number = random.randint (0,9) 

        lottery_numbers.append(number)

    lottery_numbers.sort()

    enter_numbers = []
    for i in range(0,3) :
        number = int(input("Enter a number between 0-9: "))
        while (number in enter_numbers or number < 0 or number > 9) :
            print("Invalid number, try again.")
            number = int(input("Enter a number between 0-9: "))

    enter_numbers.append(number)

    print("Today's lottery numbers are: ")
    print(lottery_numbers)

    got_number = 0
    for number in enter_numbers :
        if number in lottery_numbers :
            got_number += 1

    print("You guessed " + str(got_number) + " number(s) correctly")


    if enter_numbers == got_number :
        print("Winner!")
    else:
        enter_numbers != got_number 
        print("Sorry, you loss!")
        print("Better luck next time.")

try_again = "y"
while try_again == "y" :
    lottery()
    try_again = input("Try again y/n? ")

        
       
  
