from unicodedata import name
import pygame
import game_config as gc
from process import TicTacToe as T
from pygame import display, event, image
from time import sleep
import Images

def initial() -> pygame.Surface:
    pygame.init()
    display.set_caption('Tic-Tac-Toe')
    screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
    print( type(screen) )
    return screen

def find_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    return row, col

def update_board_display(screen : pygame.Surface, Game : T ):#Update only
    screen.blit(image.load('assets/blank.png'), (0, 0))
    #sleep(1)
    screen.fill((0, 0, 0))
    for i in range(gc.NUM_TILES_SIDE):
        for j in range(gc.NUM_TILES_SIDE):
            tile = Images.Image(Game.board[i][j])
            screen.blit(tile.image, (j * gc.IMAGE_SIZE + gc.MARGIN, i * gc.IMAGE_SIZE + gc.MARGIN))
    display.flip()
    #sleep(1)

def run(Game : T,screen : pygame.Surface, running : bool):
    while running:
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col = find_xy(mouse_x, mouse_y)
                if row >= gc.NUM_TILES_SIDE or col >= gc.NUM_TILES_SIDE:
                    continue
                if Game.MoveRecord(row,col) == True:
                    val = Game.CheckWin()
                if val == 1:
                    running = False
                    print('You Win!')
                    screen.blit(image.load('assets/win.png'), (0, 0))
                elif val == 0:
                    running = False
                    print('You Lose!')
                    screen.blit(image.load('assets/lose.png'), (0, 0))
                else:
                    Game.NextMove()
                    update_board_display(screen=screen,Game=Game)
                display.flip()
                sleep(2.1)

            
    # Display 
    screen.fill((0, 0, 0))

def play():
    screen = initial()
    running = True
    Game = T("X",gc.NUM_TILES_SIDE)
    run(Game,screen,running)

if __name__ == "__main__":

    print("Hello World!")
    play()
    print('Goodbye!')

