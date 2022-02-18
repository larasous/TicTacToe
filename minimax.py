from tic_tac_toe import empty, token, checkWinner

def movementAi(board, player):
    
    positions = takePositions(board)
    best_value = None
    best_move = None
    
    for position in positions:
        
        board[position[0]][position[1]] = token[player]
        value = minimax(board, player)
        board[position[0]][position[1]] = empty
        
        if(best_value is None):
            
            best_value = value
            best_move = position
        
        elif(player == 0):
            
            if(value > best_value):
                
                best_value = value
                best_move = position
        
        elif(player == 1):
            if(value < best_value):
                
                best_value = value
                best_move = position
    print("\nPLAYER 'O' - AI")
    print("AI PLAYED IT'S YOUR TURN\n")
    return best_move[0], best_move[1]


def takePositions(board):
    positions = []
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == empty):
                positions.append([i, j])
    
    return positions

scores = {
    "TIED GAME": 0,
    "X": 1,
    "O": -1,
}


def minimax(board, player):
    winner = checkWinner(board)
    
    if(winner):
        return scores[winner]
    
    player = (player + 1) % 2
    
    positions = takePositions(board)
    best_value = None
    
    for position in positions:
        
        board[position[0]][position[1]] = token[player]
        value = minimax(board, player)
        board[position[0]][position[1]] = empty
        
        if(best_value is None):
            
            best_value = value
        
        elif(player == 0): # player X --> 1
            
            if(value > best_value):
                
                best_value = value
        
        elif(player == 1): # player O --> -1
            if(value < best_value):
                
                best_value = value
    
    return best_value
