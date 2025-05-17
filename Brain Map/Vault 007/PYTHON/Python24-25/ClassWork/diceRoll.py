#Assignment: DiceRoll
#Author: Arslan Khan
#File name: diceRoll.py
#Contrib Auth: NONE
#Version: v1. (2024_02_22) (YYYY_MM_DD)
#==========================================================#
#Project Description:
#==========================================================#
'''
This project will take in user  given die count and sides and a function will send the result
The program will also detect if the roll was a critical failure or crtical hit (max number)
'''
#==========================================================#
# ::Variables::
#userDiceNumber holds the amount of how many dices to roll
#userSideNumber holds how many sides the dice will have
#total holds the number of total added values of the rolled dice
#ranNum holds the random number the dice roll will gives depending on the input sides never going above 20

# ::Logic::
# use the userinput to of sides and numbers to send to a function that performs the opertaion of rolling a die

import random

#define a function that will be uses with random
def diceRoll(times,sides):
    total = 0
    #define a while loop that will run until a value of zero is met which is also how man times the user wants it to run

    while times != 0:
    #make sure to uses SIDES here so you only run that many numbers!
    #This is the way through ran num that this loop gives an answer
        ranNum = random.randint(1, sides)

        print(f'Rolling a {sides} sided die...\U0001F3B2 \n'
              f'Rolled a: {ranNum} ')
    #A match case that will match with the required result
        match ranNum:
            case 1:
                print("Critical Failure!")
            case 20:
                print("Critical Hit!")
        #decrement the times calue to run it the proper amount of times
        times -= 1
        #add the total with ranNum and keep doing it until the end of the loop
        total += ranNum

    print("=" * 20)
    print(f'Total is {total}')



#ask the user for how many dices to roll?
userDiceNumber = int(input("How many die's would you like to roll: "))

#ask the user how many SIDES should the die have!
userDiceSides = int(input("How many sides will the die's have: "))

#call the function which takes in two arguments, 1 on how many dies to roll and how many sides.


#print out the results of the functions
print()
diceRoll(userDiceNumber,userDiceSides)