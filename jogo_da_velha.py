import pygame as pg
import math
import pandas as pd

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (150, 150, 150)
green = (0, 255, 0)

# Setup Window of game
window = pg.display.set_mode((1000, 600))
window.fill(black)

# Font inicializing 
font = pg.font.init()
# Choosing font family and font size
font = pg.font.SysFont("Comic Sans MS", 30)

board_array = [['n', 'n', 'n'],
               ['n', 'n', 'n'],
               ['n', 'n', 'n']]

# Click variable
click_last_status = 0
# Click on and off variable
click_on_off = 0
# Click position variable
click_position_x = -1
click_position_y = -1
# O or Y Turn
x_or_o_turn = 'x'
# End game
end_game = 0

def grid(window):
    pg.draw.rect(window, gray, (0, 0, 600, 600))
    pg.draw.line(window, white, (170, 40), (170, 555), 10)
    pg.draw.line(window, white, (405, 40), (405, 555), 10)
    pg.draw.line(window, white, (40, 170), (555, 170), 10)
    pg.draw.line(window, white, (40, 405), (555, 405), 10)
    
def click_logic(click_on_off, click_last_status, x, y):
    if click[0] == 0 and click_last_status == 1:
        click_on_off = 1
        x = (math.ceil(mouse[0] / 200) - 1)
        y = (math.ceil(mouse[1] / 200) - 1)
    elif click[0] == 0 and click_last_status == 0:
        click_on_off == 0
        x = -1
        y = -1
    return click_on_off, click_last_status, x, y

def draw_selected_cell(window, board_array):
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] == 'x':
                jogador_x(window, n, nn)
            elif board_array[nn][n] == 'o':
                jogador_o(window, n, nn)
            else:
                pass

def board_array_data(board_array, x_or_o_turn, end_game, x, y):
    if x < 3 and y < 3:
        if x_or_o_turn == 'x' and board_array[y][x] == 'n' and x != -1 and y != 1 and end_game == 0:
            board_array[y][x] = 'x'
            x_or_o_turn = 'o'
        if x_or_o_turn == 'o' and board_array[y][x] == 'n' and x != -1 and y != 1 and end_game == 0:
            board_array[y][x] = 'o'
            x_or_o_turn = 'x'
              
    return board_array, x_or_o_turn
    
def win_line(window, board_array, end_game, x_or_o_turn):
    if board_array[0][0] == 'x' and board_array[0][1] == 'x' and board_array[0][2] == 'x' \
    or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, green, (30, 100), (570, 100), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[1][0] == 'x' and board_array[1][1] == 'x' and board_array[1][2] == 'x' \
    or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
        pg.draw.line(window, green, (30, 300), (570, 300), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x' \
    or board_array[2][0] == 'o' and board_array[2][1] == 'o' and board_array[2][2] == 'o':
        pg.draw.line(window, green, (30, 500), (570, 500), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[0][0] == 'x' and board_array[1][0] == 'x' and board_array[2][0] == 'x' \
    or board_array[0][0] == 'x' and board_array[1][0] == 'x' and board_array[2][0] == 'o':
        pg.draw.line(window, green, (100, 30), (100, 580), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[0][1] == 'x' and board_array[1][1] == 'x' and board_array[2][1] == 'x' \
    or board_array[0][1] == 'x' and board_array[1][1] == 'x' and board_array[2][1] == 'o':
        pg.draw.line(window, green, (300, 30), (300, 580), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[0][2] == 'x' and board_array[1][2] == 'x' and board_array[2][2] == 'x' \
    or board_array[0][2] == 'x' and board_array[1][2] == 'x' and board_array[2][2] == 'o':
        pg.draw.line(window, green, (500, 30), (500, 580), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    elif board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'x' \
    or board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'o':
        pg.draw.line(window, green, (30, 30), (580, 580), 10)
        end_game = 1
        x_or_o_turn = 'x'
    
    elif board_array[0][2] == 'x' and board_array[1][1] == 'x' and board_array[2][0] == 'x' \
    or board_array[0][2] == 'x' and board_array[1][1] == 'x' and board_array[2][0]  == 'o':
        pg.draw.line(window, green, (580, 30), (30, 580), 10)
        end_game = 1
        x_or_o_turn = 'x'
        
    return end_game, x_or_o_turn

def restart_button(window):
    pg.draw.rect(window, gray, (700, 100, 200, 65))
    texto = font.render('Restart', 1, black)
    window.blit(texto, (750, 110))

def restart_game(board_array, x, y, end_game, click_on_off):
    if click_on_off == 1 and end_game == 1:
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            board_array = [['n', 'n', 'n'],
               ['n', 'n', 'n'],
               ['n', 'n', 'n']]
            end_game = 0
            
    return board_array, end_game

def game_status(board_array, x_or_o_turn, end_game):
    count = 0
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] != 'n':
                count += 1
    if count == 9 and x_or_o_turn == 'x':
        x_or_o_turn = 'o'
        end_game = 1
    elif count == 9 and x_or_o_turn == 'o':
        x_or_o_turn = 'x'
        end_game = 1
        
    return end_game, x_or_o_turn

def jogador_x(window, x, y):
    pg.draw.line(window, red, ((x * 200) + 30, (y * 200) + 30), ((x * 200) + 180, (y * 200) + 180), 10)
    pg.draw.line(window, red, ((x * 200) + 180, (y * 200) + 30), ((x * 200) + 30, (y * 200) + 180), 10)
    
def jogador_o(window, x, y):
    pg.draw.circle(window, blue, ((x * 200) + 105, (y * 200) + 105), 75)
    pg.draw.circle(window, gray, ((x * 200) + 105, (y * 200) + 105), 65)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            
    # Variable of mouse position
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    # print(mouse, math.ceil(mouse[0] / 200) - 1, math.ceil(mouse[1] / 200) - 1)
        
    # Variable of mouse click (click-left, click-scroll, click-right)
    click = pg.mouse.get_pressed()
    # print(click)
    
    # Game
    grid(window)
    
    click_on_off, click_last_status, click_position_x, click_position_y = click_logic(
        click_on_off, click_last_status,
        click_position_x,click_position_y)
    
    draw_selected_cell(window, board_array)
    
    board_array, x_or_o_turn = board_array_data(board_array, x_or_o_turn, end_game, click_position_x, click_position_y)
    
    end_game, x_or_o_turn = win_line(window, board_array, end_game, x_or_o_turn)
    
    restart_button(window)
    
    board_array, end_game = restart_game(board_array, mouse_position_x, mouse_position_y, end_game, click_on_off)
    
    end_game, x_or_o_turn = game_status(board_array, x_or_o_turn, end_game)
    
    restart_button(window)
    
    # Click last status
    if click[0] == 1:
        click_last_status = 1
    else:
        click_last_status = 0
    
    pg.display.update()