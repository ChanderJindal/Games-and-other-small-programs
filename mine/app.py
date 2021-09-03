import pygame
import game_config as gc
import mineswipper as game
from pygame import display, event, image
from time import sleep
import animal
#from animal import Animal

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
display.set_caption('My Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
running = True

board = game.BOX(gc.NUM_TILES_SIDE,gc.MINES)
visible_part = board.visible_part()
actual_part = board.actual_board()

tiles = [[None for _ in range(gc.NUM_TILES_TOTAL)] for _ in range(gc.NUM_TILES_TOTAL)]
for i in range(gc.NUM_TILES_SIDE):
    for j in range(gc.NUM_TILES_SIDE):
        tiles[i][j] = animal.Image(i,j,actual_part[i][j])

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
            row, col, index = find_index_from_xy(mouse_x, mouse_y)
            if (row,col) not in board.checked:
                board.dig(row,col)
                

    # Display animals
    screen.fill((0, 0, 0))


    for i in range(gc.NUM_TILES_SIDE):
        for j in range(gc.NUM_TILES_SIDE):
            tile = tiles[i][j]
            current_image = tile.image if (i,j) in board.checked else tile.box
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))

    display.flip()

    if len(board.checked) == gc.NUM_TILES_TOTAL - gc.MINES:
        running = False
        screen.blit(image.load('assets/12.png'), (0, 0))

print('Goodbye!')

'''
    # Check for matches
    if len(current_images_displayed) == 2:
        idx1, idx2 = current_images_displayed
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            # display matched message
            sleep(0.2)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.5)
            current_images_displayed = []
'''

