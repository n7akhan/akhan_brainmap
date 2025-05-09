import random
#A simple program to guess a number
#you ask here once but you MUST ask inside the loop as well because the guess value will never change if you dont ask again.
guess = int(input("Guess a number between 1 and 10: "))
random_num = random.randint(1,10)

while guess != random_num:
    if guess < random_num:
        print("You are too low! Try again! ")
    elif guess > random_num:
        print("You are too high! Try again!")
    guess = int(input("Guess a number between 1 and 10: "))

print("BINGO YOU GOT IT! ")
