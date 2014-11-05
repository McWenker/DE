import pygame, sys
from pygame.locals import *
from constants import *
from random import choice
from screen import Screen
from map import Map

# initialize that shit
pygame.init()
font = pygame.font.Font(None, 18)
FPS_clock = pygame.time.Clock()
map = Map()
screen = Screen()

# store coords of mouse
mouse_x = 0 
mouse_y = 0

# 0 = impassable, for now
passable_tiles = map.get_passable_tiles(False)
main_board = map.generate_map()

def terminate():
	pygame.quit()
	sys.exit()

## MAIN GAME LOOP ##
while True:
	mouse_click = False
	screen.screen.fill(BLACK)
	screen.draw_board(main_board, passable_tiles)
	
	for event in pygame.event.get(): # event handle loop
		if event.type == QUIT or (event.type == K_UP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouse_x, mouse_y = event.pos
		elif event.type == MOUSEBUTTONUP:
			mouse_x, mouse_y = event.pos
			mouse_click = True
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				terminate()
			
		tile_x, tile_y = screen.get_tile_at_pixel(mouse_x, mouse_y)
		if tile_x != None and tile_y != None:
			# the mouse is over a box
			screen.draw_highlight_box(tile_x, tile_y)
			if not passable_tiles[tile_x][tile_y] and mouse_click:
				passable_tiles[tile_x][tile_y] = True # set tile as passable
			elif passable_tiles[tile_x][tile_y] and mouse_click:
				passable_tiles[tile_x][tile_y] = False
				
		# redraw screen
		pygame.display.update()
		FPS_clock.tick(FPS)