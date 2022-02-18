token = ['X', 'O']
empty = ' '

def createBoard():
    board = [
        [empty, empty, empty],
        [empty, empty, empty],
        [empty, empty, empty],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i < 2):
            print("------")


def getInputValid(message):
    try:
        op = int(input(message))
        if(op >= 1 and op <= 3):
            return op - 1
        else:
            print("O número precisa ser entre 1 e 3")
            return getInputValid(message)
    except:
        print("Insira um número válido!")
        return getInputValid(message)


def checkMovement(board, row, column):
    if(board[row][column] == empty):
        return True
    else:
        return False


def makeMovement(board, row, column, op):
    board[row][column] = token[op]


def checkWinner(board):
    # verifica as linhas
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != empty):
            return board[i][0]
    
    # verifica as colunas    
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != empty):
            return board[0][i]
        
    # verifica a diagonal principal
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != empty):
        return board[0][0]
    
    # verifica a diagonal secundária
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != empty):
        return board[0][2]
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == empty):
                return False
    
    return "TIED GAME"