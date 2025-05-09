import random
#Counter for the loop itaration
maxAttempt = 6
counter = 0
#Declare a list with random words
myList = ["hello","linux","apple","computer","amazing"]
#call the random method to choose random word
random_word = random.choice(myList)
#Break down the word into single characters using a list function
WordList = list(random_word)
#Visually represent the word by the length of the word
display = ['_'] * len(WordList)
print(f"Can you guess the word but guessing the letters! You have {maxAttempt} attempts!")
#An empty list that takes in guessed letters and tracks them
guessed_letters = []


while counter < maxAttempt:
    #take in guess with .lower method
    guess = input("Enter the letter of the word!: ").lower()

    #Check to see if guess is a single character or not
    if len(guess) > 1:
        print("Please choose a single character!")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter! Try again!")
        continue
    #add the letter in the list to track later
    guessed_letters.append(guess)

    #if the guess exists in WordList then add to display
    if guess in WordList:
        for i in range (len(WordList)):
            if WordList[i] == guess:
               display[i] = guess
               print("Great guess!")
               print(display)

    #if the guess does not exist in WordList then counter goes up and re try
    else:
        counter += 1
        print(f"Letter does not exist in list! You have {maxAttempt - counter} attempts left!")
        continue
    if display == WordList:
        print(f"Congrats! The word was guessed correctly! The word was {random_word} and it took you {counter} attempts!")
        break

else:
    print(f"Sorry Max Attempts reached! Attempts used {counter}. The word was {random_word}")



