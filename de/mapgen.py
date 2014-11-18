import pygame, math, sys, random
from pygame.locals import *
from random import randint, choice
from constants import *
from tile import Tile

class Map(object):
	# stores values for map grid
	#
	# Map.passable = passable tile (0)
	def __init__(self):
		# sets all tiles to passable
		self.terrain = self.generate_map()
	
	def generate_map(self):
		# returns a map with all values set to 0
		game_map = []
		for i in range(ROWS):
			row = []
			for j in range(COLUMNS):
				x = randint(0,4)
				if x == 0:
					row.append(Tile(pos=(i,j), terrain='Dirt'))
				elif x == 1:
					row.append(Tile(pos=(i,j), terrain='Grass'))
				elif x == 2:
					row.append(Tile(pos=(i,j), terrain='Water'))
				else:
					row.append(Tile(pos=(i,j), terrain='Rock'))
			game_map.append(row)
		return game_map
		
	def get_passable_tiles(self, val):
		pass_boxes = []
		for i in range(COLUMNS):
			pass_boxes.append([val] * ROWS)
		return pass_boxes
		