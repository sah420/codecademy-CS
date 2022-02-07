board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = 'X'
winner = None
gameRunning = True

# player class
class Player:
    def __init__(self, name, sign, winner = False):
        self.name = name
        self.winner = winner
        self.sign = sign
        
    def __repr__(self):
        return self.name

    
#printing the board
def printBoard(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# taking player input
def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    
    if inp >= 1 and inp <= 9 and board[inp - 1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Oops! Looks like your opponent is in that spot.')

# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        if board[0] == "X":
            player1.winner = True
            return True
        else:
            player2.winner = True
            return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        if board[0] == "X":
            player1.winner = True
            return True
        else:
            player2.winner = True
            return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        if board[0] == "X":
            player1.winner = True
            return True
        else:
            player2.winner = True
            return True
        



player1 = Player("Player 1 (X)", "X", False)
player2 = Player("Player 2 (O)", "O", False)


printBoard(board)
playerInput(board)
printBoard(board)


