from tic_tac_toe import createBoard, printBoard, getInputValid, checkWinner, checkMovement, makeMovement
from minimax import movementAi

board = createBoard()
winner = checkWinner(board)

player = 0 # player X

while(not winner):
    print("="*6)
    printBoard(board)
    print("="*6)
    
    if(player == 0):
        print("\nPLAYER 'X'")
        row = getInputValid("- Informe a linha: ")
        column = getInputValid("- Informe a coluna: ")
        print()
    else:
        row, column = movementAi(board, player) 
    
    if(checkMovement(board, row, column)):
        
        makeMovement(board, row, column, player)
        
        player = (player + 1) % 2
        
    else:
        print("A posição já está ocupada")
    
    winner = checkWinner(board)

print("="*10)
if(winner in "O"):
    print("The winner was AI - Player", winner)
elif(winner in "X"):
    print("The winner was you - Player", winner)
else:
    print(winner)
print("="*10)