board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

def placer(row, col, sign):
    if 0 <= row < 6 and 0 <= col < 7 and (sign == 'x' or sign == 'o'):
        if board[row][col] == ' ':
            board[row][col] = sign
        else:
            print("Position already occupied!")
    else:
        print("Enter a valid position (0-5 for row, 0-6 for col) and valid sign ('x' or 'o').")

def print_board():
    """Print the Connect Four board."""
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---+---+---+---+---+---+---+')

def logic_finder(board, sign):
    rows = len(board)
    cols = len(board[0])


    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] == sign and board[row][col+1] == sign and board[row][col+2] == sign and board[row][col+3] == sign:
                return True

    for row in range(rows - 3):
        for col in range(cols):
            if board[row][col] == sign and board[row+1][col] == sign and board[row+2][col] == sign and board[row+3][col] == sign:
                return True
            
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] == sign and board[row+1][col+1] == sign and board[row+2][col+2] == sign and board[row+3][col+3] == sign:
                return True

    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] == sign and board[row+1][col+1] == sign and board[row+2][col+2] == sign and board[row+3][col+3] == sign:
                return True
            
    for row in range(rows - 3):
        for col in range(3, cols):
            if board[row][col] == sign and board[row+1][col-1] == sign and board[row+2][col-2] == sign and board[row+3][col-3] == sign:
                return True
    return False

turn = 1  # Player turn: 1 for 'x', 2 for 'o'
while True:
    print_board()
    try:
        row = int(input(f"Player {turn} - Enter the row (0-5): "))
        col = int(input(f"Player {turn} - Enter the column (0-6): "))
        sign = 'x' if turn == 1 else 'o'
        placer(row, col, sign)

        if logic_finder(board, sign):
            print_board()
            print(f"Player {turn} ({sign}) WON!!!!!!")
            break

        turn = 3 - turn 
    except ValueError:
        print("Invalid input. Please enter numbers for row and column.")
