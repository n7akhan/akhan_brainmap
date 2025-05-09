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
board = ["1", "O", "3", "4", "5", "6", "7", "8", "9","10"]

print("=============HERE IS OUR BOARD!!!=============")
print(board[0], "|", board[1], "|", board[2])
print("-" * 10)
print(board[3], "|", board[4], "|", board[5])
print("-" * 10)
print(board[6], "|", board[7], "|", board[8])

while True:
    #WE use -1 to make sure the position is what we see! in binary everything starts at 0
    while True:
        playerOnePosition = int(input("Player ONE enter what position: "))
        if board[playerOnePosition - 1] == playerTwoInt:
            print("INVALID PLAYER ONE!")
            break
    else:
        board[playerOnePosition - 1] = playerOneInt






        print(board[0], "|", board[1], "|", board[2])
        print("-" * 10)
        print(board[3], "|", board[4], "|", board[5])
        print("-" * 10)
        print(board[6], "|", board[7], "|", board[8])

    playerTwoPosition = int(input("Player TWO enter what position: "))
    if board[playerTwoPosition -1 ] == playerOneInt:
        print("INVALID PLAYER TWO")
    else:
      board[playerTwoPosition - 1] = playerTwoInt

       # print(board[0], "|", board[1], "|", board[2])
        #print("-" * 10)
        #print(board[3], "|", board[4], "|", board[5])
        #print("-" * 10)
        #print(board[6], "|", board[7], "|", board[8])
