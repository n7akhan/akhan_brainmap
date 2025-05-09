board = ["X", "2", "3", "4", "X", "6", "7", "8", "X","10"]


winningCombo = [
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6)
    ]
for combo in winningCombo:
#IMPORTANT! the combo [0] combo [1] combo [2] is giving the respectiive colloum indicies to board[]
#So combo [0] is really saying board[0] = then combo[0] from combo [3] is saying board[3] which is 4

      if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            print("winner")