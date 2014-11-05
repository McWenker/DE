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
		self.passable = self.generate_map()
	
	def generate_map(self):
		# returns a map with all values set to 0
		map = []
		for i in range(ROWS):
			row = []
			for j in range(COLUMNS):
				row.append(Tile(pos=(i,j)))
			map.append(row)
		return map
		
	def get_passable_tiles(self, val):
		pass_boxes = []
		for i in range(COLUMNS):
			pass_boxes.append([val] * ROWS)
		return pass_boxes
		