import pygame
from constants import *
from map import Map
import textStyle

class Screen(object):
	# draws the map and sprites to screen
	#
	
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('SPACE TYCOON')

	def draw_board(self, board, passable):
		# draws all boxes in covered or revealed state
		for tile_x in range(COLUMNS):
			for tile_y in range(ROWS):
				left, top = self.top_left_convert(tile_x, tile_y)
				if not passable[tile_x][tile_y]:
					# draw red, impassable tile
					pygame.draw.rect(self.screen, RED, (left, top, TILE_SIZE, TILE_SIZE))
				else:
					# draw blue, passable tile
					pygame.draw.rect(self.screen, BLUE, (left, top, TILE_SIZE, TILE_SIZE))
					
	def top_left_convert(self, tile_x, tile_y):
		# convert board coords into pixel coords
		left = tile_x * (TILE_SIZE + GAP_SIZE) + X_MARG
		top = tile_y * (TILE_SIZE + GAP_SIZE) + Y_MARG
		return (left, top)
		
	def get_tile_at_pixel(self, x, y):
		for tile_x in range(COLUMNS):
			for tile_y in range(ROWS):
				left, top = self.top_left_convert(tile_x, tile_y)
				tile_rect = pygame.Rect(left, top, TILE_SIZE, TILE_SIZE)
				if tile_rect.collidepoint(x, y):
					return(tile_x, tile_y)
		return(None, None)
				
	def draw_highlight_box(self, tile_x, tile_y):
		left, top = self.top_left_convert(tile_x, tile_y)
		pygame.draw.rect(self.screen, WHITE, (left-5, top-5, TILE_SIZE+10, TILE_SIZE+10),4)

	def drawList(self, list, lineHeight, loc):
		for item in list:
			self.screen.blit(item, loc)
			loc[1] += lineHeight

	def drawText(self, text, loc):
		self.screen.blit(text, loc)
