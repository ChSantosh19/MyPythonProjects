import random
import sys

BLANK_SPACE = '  '

def main():
    print('Number sliding game!')
    print("""Use the WASD keys to move the tiles
            back into their original order:
            1 2 3 4
            5 6 7 8
            9 10 11 12
            13 14 15""")
    
    gameBoard = getNewPuzzel()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()

def getNewBoard():
    return [['1 ', '2 ', '3 ', '4 '], 
            ['5 ', '6 ', '7 ', '8 '], 
            ['9 ', '10', '11', '12'], 
            ['13', '14', '15', BLANK_SPACE]]

def displayBoard(board):
    labels = [board[0][0], board[0][1], board[0][2], board[0][3],
              board[1][0], board[1][1], board[1][2], board[1][3],
              board[2][0], board[2][1], board[2][2], board[2][3],
              board[3][0], board[3][1], board[3][2], board[3][3]]
    
    boardToDraw = """
+------+------+------+------+ 
|  {}  |  {}  |  {}  |  {}  |
+------+------+------+------+
|  {}  |  {}  |  {}  |  {}  |
+------+------+------+------+
|  {}  |  {}  |  {}  |  {}  |
+------+------+------+------+
|  {}  |  {}  |  {}  |  {}  |
+------+------+------+------+
""".format(*labels)
    print(boardToDraw)

def findBlankSpace(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == BLANK_SPACE:
                return i, j

def askForPlayerMove(board):
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blankx != 0 else ' '
    a = 'A' if blanky != 0 else ' '
    s = 'S' if blankx != 3 else ' '
    d = 'D' if blanky != 3 else ' '

    while True:
        print(f'                           ({w})')
        print(f'Enter WASD (or QUIT): ({a}) ({s}) ({d})')

        response = input('>>> ').upper()
        if response == "QUIT":
            sys.exit()

        if response in (w + a + s + d).replace(' ', ''):
            return response

def makeMove(board, move):
    bx, by = findBlankSpace(board)

    if move == 'W' and bx > 0:
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]
    elif move == 'A' and by > 0:
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'S' and bx < 3: 
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'D' and by < 3:
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]

def makeRandomMove(board):
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blankx > 0:
        validMoves.append('W')
    if blanky > 0:
        validMoves.append('A')
    if blankx < 3:
        validMoves.append('S')
    if blanky < 3:
        validMoves.append('D')
    
    makeMove(board, random.choice(validMoves))

def getNewPuzzel(move=200):
    board = getNewBoard()

    for _ in range(move):
        makeRandomMove(board)
    return board

if __name__ == '__main__':
    main()
