#==============================================================#
#define a function that displays a tic tac toe board
#==============================================================#
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("-" * 10)
    print(board[3], "|", board[4], "|", board[5])
    print("-" * 10)
    print(board[6], "|", board[7], "|", board[8])

#==============================================================#
#define a function that checks the board for winners with player input and the winning combo tulpes
#==============================================================#
def check_winner(board,player):
    winningCombo = [
        (0, 1, 2), #ROW
        (3, 4, 5), #ROW
        (6, 7, 8), #ROW
        (0, 3, 6), #COLUMN
        (1, 4, 7), #COLUMN
        (2, 5, 8), #COLUMN
        (0, 4, 8), #DIAGONAL
        (2, 4, 6) #DIAGONAL
    ]
    for combo in winningCombo:
        #==========================================================================================================#
        # IMPORTANT! the combo [0] combo [1] combo [2] is giving the respective column indices to board[]
        # So combo [0] is really saying board[0] = then combo[0] from combo [3] is saying board[3] which is 4
        # Now we also check player symbol too to return true if there is a winner! Else explicitly return a False
        # "Each combo gives us 3 positions on the board.
        # For example, the combo (0, 3, 6) means we're checking board[0], board[3], and board[6].
        # Those are the vertical column from top to bottom on the left side."
        #==========================================================================================================#
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


#==============================================================#
#Here I declare a counter variable
#==============================================================#

moveCount = 0

print("WELCOME TO TIC THEN TAC THEN TOE!")

#=============================================================================================================================#
#Here we check to make sure that entered items are in list of X and O only and assign the OTHER shape to player two by default
#==============================================================================================================================#
while True:

    playerOneInt = input("Please pick your shape, either 'X' or 'O': ").upper()
    if playerOneInt not in ["X","O"]:
        print(" INVALID!!! please pick a correct shape X or O! ")
    else:
        break

#==============================================================#
#Assign the players there shapes!
#==============================================================#
if playerOneInt == 'X':
    playerTwoInt = 'O'
else:
    playerTwoInt = 'X'
print(f'Player Two got {playerTwoInt} shape!')

#==============================================================#
#print out the board that the game will be played on!
#==============================================================#
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("=============HERE IS OUR BOARD!!!=============")

#===================================================================#
#The main while loop that will run the game and break at win and draw
#===================================================================#
while True:
    print_board()

    #==============================================================#
    #TRAP the user's input if its a symbol and not a number 1-9
    #==============================================================#
    while True:
        playerOnePosition = input("Player ONE pick a position: ")
        if not playerOnePosition.isdigit(): #This check if the input is a digit or an alphabet
            print("INVALID! Pick a number between 1-9!!!")
            continue
        else:
            playerOnePosition = int(playerOnePosition) #Converts string intput to integer!

            if playerOnePosition not in range(1,10):
                print("INVALID OPTION!")
                #Check if position is taken by player 2
            elif board[playerOnePosition - 1] == playerTwoInt:

                print("Position taken! Pick another!")
                print_board()
                #Check if current player has taken that position or not
            elif board[playerOnePosition - 1] == playerOneInt:
                print("You already took that position!")
                print_board()
                #This assigns the position
            else:
                board[playerOnePosition -1] = playerOneInt
                break
    moveCount +=1
    print_board()
    if check_winner(board,playerOneInt):
        print("Player 1 has won!")
        break
    if moveCount == 9:
        print("its a draw!")
        break

    while True:
        playerTwoPosition = input("Player TWO pick a position: ")
        if not playerTwoPosition.isdigit():  # This check if the input is a digit or a aplhabet
            print("INVALID! Pick a number between 1-9!!!")
            continue
        else:
            playerTwoPosition = int(playerTwoPosition)  # Converts string intput to integer!

            if playerTwoPosition not in range(1, 10):
                print("INVALID OPTION!")
            elif board[playerTwoPosition - 1] == playerOneInt:

                print("Position taken! Pick another!")
                print_board()
            elif board[playerTwoPosition - 1] == playerTwoInt:
                print("You already took that position!")
                print_board()
            else:
                board[playerTwoPosition - 1] = playerTwoInt
                break
    moveCount += 1
    if check_winner(board,playerTwoInt):
        print("Player 2 has won!")
        break
    if moveCount == 9:
        print("its a draw!")
        break

