from random import randrange
from time import sleep

turn_X_O = 'X'

running = True

# Create a board of game
def create_board():
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# Show board on screen
def display_board(board):
    for n in range(3):
        for i in range(3):
            print("+" + "-" * 7, end="")
        print("+")
        for i in range(3):
            print("|" + " " * 7, end="")
        print("|")
        for nn in range(3):
            print("|" + " " * 3 + f"{board[n][nn]}" + " " * 3, end="")
        print("|")
        for i in range(3):
            print("|" + " " * 7, end="")
        print("|")
    for i in range(3):
        print("+" + "-" * 7, end="")
    print("+")

# Generate random number for machine play
def random_position():
    return randrange(1, 10)

def verify_empty_squares(positon, value_x_or_o):
    for row in range(0, 3):
        for column in range(0, 3):
            square = board[row][column]
            if positon == square and square != 'X' and square != 'O':
                board[row][column] = value_x_or_o
                return True
    print("This square is filled")
    return False

# Machine turn
def machine_turn(board):
    pos_filled = False
    
    while pos_filled == False:
        random_pos = random_position()    
        pos_filled = verify_empty_squares(random_pos, 'X')

def valid_input_user(input_user):
    for n in range(1, 10):
        if input_user == n:
            return True
    print("Out of range")
    return False
    
# Player turn
def player_turn(board):
    pos_filled = False
    
    while pos_filled == False:
        try:
            selected_pos = int(input("Enter your move: "))            
        except ValueError:
            print("This is invalid value")
            continue
        
        if valid_input_user(selected_pos):
            pos_filled = verify_empty_squares(selected_pos, 'O')
                    

def results_standarts(board, value_x_or_o):
    if board[0][0] == value_x_or_o and board[0][1] == value_x_or_o and board[0][2] == value_x_or_o or \
    board[1][0] == value_x_or_o and board[1][1] == value_x_or_o and board[1][2] == value_x_or_o or \
    board[2][0] == value_x_or_o and board[2][1] == value_x_or_o and board[2][2] == value_x_or_o or \
    board[0][0] == value_x_or_o and board[1][0] == value_x_or_o and board[2][0] == value_x_or_o or \
    board[0][1] == value_x_or_o and board[1][1] == value_x_or_o and board[2][1] == value_x_or_o or \
    board[0][0] == value_x_or_o and board[1][1] == value_x_or_o and board[2][2] == value_x_or_o or \
    board[0][2] == value_x_or_o and board[1][1] == value_x_or_o and board[2][0] == value_x_or_o:
        return True
    return False

# # Verify if player won
# def player_result(board):
#     if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or \
#     board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or \
#     board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or \
#     board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or \
#     board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
#     board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
#     board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
#         return True
#     return False

# # Verify if machine won
# def machine_result(board):
#     if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or \
#     board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or \
#     board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or \
#     board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or \
#     board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
#     board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
#     board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
#         return True
#     return False

# Verify if draw
def draw(board, p_result, m_result):
    for row in range(0, 3):
        for column in range(0, 3):
            square = board[row][column]
            if square != 'X' and square != 'O':
                return False
    if p_result == False and m_result == False:
        return True
    

board = create_board()
p_result = False
m_result = False

while running:
    
    if turn_X_O == 'X':
        machine_turn(board)
        turn_X_O = 'O'
        display_board(board)
   
    m_result = results_standarts(board, 'X')
    
    if draw(board, p_result, m_result):
        print("Draw!")
        break
        
    if m_result:
        print("You lose!")
        break
        
    if turn_X_O == 'O':
        player_turn(board)
        turn_X_O = 'X'
        display_board(board)
            
    p_result = results_standarts(board, 'O')
    
    if p_result:
        print("You won!")
        break
        
    sleep(2)
       
"""
Board prototipe

+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
"""