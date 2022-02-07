board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
winner = False
gameRunning = True
winnerz = ''

# player class
class Player:
    def __init__(self, name, sign, winning = False):
        self.name = name
        self.winning = winning
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
    inp2 = int(input("Enter a number between 1-9: "))

    if inp2 >= 1 and inp2 <= 9 and board[inp2 - 1] == '-':
        board[inp2-1] = currentPlayer
    else:
        print('Oops! Looks like your opponent is in that spot.')

def whichPlayer(board):
    global currentPlayer
    inp1 = int(input("Are you player 1 or 2? (Enter either 1 or 2): "))
    
    if inp1 == 1:
        currentPlayer = player1.sign
        playerInput(board)
    elif inp1 == 2:
        currentPlayer = player2.sign
        playerInput(board)
    else:
        print('Oops! Looks like your trying to play using an imaginary player. Please pick 1 or 2.')

# check for win or tie
def checkHorizontal(board):
    global winnerz
    if board[0] == board[1] == board[2] and board[0] != '-':
        if board[0] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        if board[3] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        if board[6] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True

            
def checkDiagonal(board):
    global winnerz
    if board[0] == board[4] == board[8] and board[0] != '-':
        if board[0] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True

    elif board[6] == board[4] == board[2] and board[6] != '-':
        if board[6] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True

            
def checkVertical(board):
    global winnerz
    if board[0] == board[3] == board[6] and board[0] != '-':
        if board[0] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True

    elif board[1] == board[4] == board[7] and board[1] != '-':
        if board[0] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        if board[0] == "X":
            winnerz = player1
            player1.winning = True
        else:
            winnerz = player2
            player2.winning = True


def checkWinner(x):
    global winner
    
    if x == True:
        winner = True
        


player1 = Player("Player 1 (X)", "X", False)
player2 = Player("Player 2 (O)", "O", False)

printBoard(board)
print('Welcome to Tic Tac Toe. You want to connect three either vertically, horizontally, or diagonally to win. Goodluck!')


while winner == False:
    whichPlayer(board)
    printBoard(board)
    checkHorizontal(board)
    checkDiagonal(board)
    checkVertical(board)
    checkWinner(player1.winning)
    checkWinner(player2.winning)
    print(winnerz)

print('Thank you for playing Tic Tac Toe. The winner for this game was {player}'.format(player = winnerz))
