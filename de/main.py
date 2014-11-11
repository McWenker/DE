import pygame, sys
from pygame.locals import *
from constants import *
from random import choice
from screen import Screen
from map import Map
from resourceManager import ResourceManager
from textStyle import TextStyle
from unit import Unit

# initialize that shit
pygame.init()

FPS_clock = pygame.time.Clock()
map = Map()


# init our units
unit = Unit(WHITE, 50, 50)
# unit_list = pygame.sprite.Group()
# unit_list.add(unit)


# init our style
textStyle = TextStyle()

# init the interface
screen = Screen()
resourceManager = ResourceManager()

# store coords of mouse
mouse_x = 0 
mouse_y = 0

# 0 = impassable, for now
passable_tiles = map.get_passable_tiles(False)
main_board = map.generate_map()
highlightBox = (None,None)

def terminate():
	pygame.quit()
	sys.exit()

sizething = 50

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
			unit.setDestination(event.pos)
		elif event.type == KEYDOWN:			
			resourceManager.add('adamantium',1)
			if event.key == K_ESCAPE:
				terminate()
			
		tile_x, tile_y = screen.get_tile_at_pixel(mouse_x, mouse_y)
		if tile_x != None and tile_y != None:
			# the mouse is over a box
			highlightBox = (tile_x, tile_y)

			if not passable_tiles[tile_x][tile_y] and mouse_click:
				passable_tiles[tile_x][tile_y] = True # set tile as passable
			elif passable_tiles[tile_x][tile_y] and mouse_click:
				passable_tiles[tile_x][tile_y] = False
		else:
			highlightBox = (None,None)

	#draw the highlight box if anything is highlighed
	if highlightBox[0] != None and highlightBox[1] != None:
		screen.draw_highlight_box(highlightBox[0], highlightBox[1])


	unit.updatePos()
	# redraw screen
	screen.drawList(resourceManager.drawResources(), textStyle.lineHeight, [50,50])
	# unit_list.draw(screen)
	screen.screen.blit(unit.image, unit.rect)
	pygame.display.update()
	FPS_clock.tick(FPS)
	