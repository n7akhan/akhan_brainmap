#IMPORT RANDOM CLASS TO USE RANDOM FUNCTION
import random

print("WELCOME TO ROCK, PAPER, SCISSOR")

#Declare the variables to ittirate scores and make a list of choices for comp
newGame = "y"
UserScore = 0
CompScore = 0
gameChoice = ["rock", "paper", "scissor"]


#This loop will not break unless n for no is inputed!

while newGame != "n":

#Declare a variable that stores in a random choice from the LIST gameChoice
    compChoice = random.choice(gameChoice)


#This loop is validation loop for the input, it checks for strings and in those strings exists in the list again and again and wont break until string entered

    while True:
        userChoice = input("Please pick rock, paper, or scissor: ").lower()
        if userChoice.isalpha() and userChoice in gameChoice:
            break
        else:
            print("Invalid! Please spell correctly and no symbols!")


#The tie case! So no score added

    if userChoice == compChoice:
        print("its a tie!")

#This is for the cases where the player wins and score is incrimated by 1

    elif (userChoice == "rock" and compChoice == "scissor") or \
         (userChoice == "paper" and compChoice == "rock") or \
         (userChoice == "scissor" and compChoice == "paper"):
        UserScore += 1
        print(f'You won! You had {userChoice} and computer had {compChoice} and {userChoice} beats {compChoice}. Your score is {UserScore} and Computers is {CompScore}')

#This is the rest of the choices case where computer will win in all otehr matters that isnt a tie or win for us

    else:
        print(f'The darn computer won! The computer had {compChoice} and {compChoice} beats {userChoice}')
        CompScore += 1

#This is just a statement to show scores


    print(f'Current score is your score {UserScore} and computers {CompScore}')

#This is a loop that helps with validating Yes or No to continue the loop!

    newGame = input("Wanna go again!? Y or N: ").lower()
    while newGame not in ["y","n"]:
        newGame = input("Invalid! Please enter Y or N: ")

#END GAME statements that uses score to output values

if UserScore > CompScore:
    print("YOU WON! GOOD BYE THAT WAS FUN!")
elif CompScore > UserScore:
    print("YOU LOST! BETTER LUCK NEXT TIME!")
else:
    print("YOU LEFT AT A TIE WOW!")
