import pygame
from constants import *
from mapgen import Map
import textStyle

class Screen(object):
	# draws the map and sprites to screen
	#
	
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('DE-3439')

	def draw_map(self, main_map, passability):
		# draws all boxes in covered or revealed state
		for tile_x in range(COLUMNS):
			for tile_y in range(ROWS):
				left, top = self.top_left_convert(tile_x, tile_y)

				if main_map[tile_x][tile_y].terrain == 'Void':
					# draw black, Void tile
					pygame.draw.rect(self.screen, BLACK, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'DeepWater':
					# draw dark blue, DeepWater tile
					pygame.draw.rect(self.screen, D_BLUE, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'ShalWater':
					# draw light blue, ShalWater tile
					pygame.draw.rect(self.screen, L_BLUE, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Dirt1':
					# draw light green, LowGrass tile
					pygame.draw.rect(self.screen, L_BROWN1, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Dirt2':
					# draw light green, HighGrass tile
					pygame.draw.rect(self.screen, L_BROWN2, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Dirt3':
					# draw light brown, ShalDirt tile
					pygame.draw.rect(self.screen, D_BROWN1, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Dirt4':
					# draw light brown, DeepDirt tile
					pygame.draw.rect(self.screen, D_BROWN2, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Rock':
					# draw light grey, Rock tile
					pygame.draw.rect(self.screen, L_GREY, (left, top, TILE_SIZE, TILE_SIZE))
				elif main_map[tile_x][tile_y].terrain == 'Granite':
					# draw dark grey, Granite tile
					pygame.draw.rect(self.screen, D_GREY, (left, top, TILE_SIZE, TILE_SIZE))

					
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
		pygame.draw.rect(self.screen, WHITE, (left-1, top-1, TILE_SIZE+2, TILE_SIZE+2),4)

	def draw_list(self, list, lineHeight, loc):
		for item in list:
			self.screen.blit(item, loc)
			loc[1] += lineHeight

	def draw_text(self, text, loc):
		self.screen.blit(text, loc)
