from random import randrange
from time import sleep

turn_X_O = 'X'

running = True

def create_board():
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

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

def random_position():
    return randrange(1, 10)

def machine_turn(board):
    pos_fill = False
    
    while pos_fill == False:
        random_pos = random_position()
        
        for row in range(0, 3):
            if pos_fill == True:
                break
            for column in range(0, 3):
                square = board[row][column]
                if random_pos == square and square != 'X' and square != 'O':
                    board[row][column] = 'X'
                    pos_fill = True
                    break
                
def player_turn(board):
    selected_pos = int(input("Enter your move: "))
    
    for row in range(0, 3):
        for column in range(0, 3):
            square = board[row][column]
            if selected_pos == square:
                board[row][column] = 'O'
                
def player_result(board):
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or \
    board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or \
    board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or \
    board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or \
    board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
    board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
    board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    return False
    
def machine_result(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or \
    board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or \
    board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or \
    board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or \
    board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
    board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
    board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    return False
    
def draw(board, p_result, m_result):
    print(p_result, m_result)
    for row in range(0, 3):
        for column in range(0, 3):
            square = board[row][column]
            if square != 'X' or square != 'O':
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
   
    m_result = machine_result(board)
    
    if draw(board, p_result, m_result):
        print("Draw!")
        running = False
        continue
        
    if m_result:
        print("You lose!")
        running = False
        continue
        
    if turn_X_O == 'O':
        player_turn(board)
        turn_X_O = 'X'
        display_board(board)
            
    p_result = player_result(board)
    
    if p_result:
        print("You won!")
        running = False
        continue
        
    sleep(2)
         
"""
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