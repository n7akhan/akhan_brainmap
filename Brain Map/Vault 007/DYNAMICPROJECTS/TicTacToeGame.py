def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("-" * 10)
    print(board[3], "|", board[4], "|", board[5])
    print("-" * 10)
    print(board[6], "|", board[7], "|", board[8])


""""
def check_winner(board):
    winningCombo = [
        (0,1,2)
    ]
    for combo in winningCombo:
        
"""


print("WELCOME TO TIC THEN TAC THEN TOE!")

#Here we check to make sure that entered items are in list of X and O only and assign the OTHER shape to player two by defaulta
while True:
    playerOneInt = input("Please pick your shape, either 'X' or 'O': ").upper()
    if playerOneInt not in ["X","O"]:
        print(" INVALID!!! please pick a correct shape X or O! ")
    else:
        break
if playerOneInt == 'X':
    playerTwoInt = 'O'
else:
    playerTwoInt = 'X'
print(f'Player Two got {playerTwoInt} shape!')

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"]


print("=============HERE IS OUR BOARD!!!=============")

while True:
    print_board()
    while True:
        playerOnePosition = input("Player ONE pick a position: ")
        if not playerOnePosition.isdigit(): #This check if the input is a digit or a aplhabet
            print("INVALID! Pick a number between 1-9!!!")
            continue
        else:
            playerOnePosition = int(playerOnePosition) #Converts string intput to integer!

            if playerOnePosition not in range(1,10):
                print("INVALID OPTION!")
                #Check if position is takne by player 2
            elif board[playerOnePosition - 1] == playerTwoInt:
                print_board()
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

    print_board()
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
                print_board()
                print("Position taken! Pick another!")
                print_board()
            elif board[playerTwoPosition - 1] == playerTwoInt:
                print("You already took that position!")
                print_board()
            else:
                board[playerTwoPosition - 1] = playerTwoInt
                break

