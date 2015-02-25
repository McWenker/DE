import pygame, math, sys, random
from util.perlin import SimplexNoise
from pygame.locals import *
from random import randint, choice
from constants import *
from tile import Tile


perlin = SimplexNoise(period=500)


class Map(object):
	# stores values for map grid
	#
	# Map.passable = passable tile (0)
	def __init__(self, island_size=50):
		# sets all tiles to passable
		self.island_size = island_size
		self.rocks = self.generate_map()
		self.

	
	def generate_map(self):
		# returns a map with all values set to 0
		game_map = []
		for i in xrange(ROWS):
			row = []
			for j in xrange(COLUMNS):
				row.append(0)
			game_map.append(row)
		return game_map
		
	def get_passable_tiles(self, val):
		pass_boxes = []
		for i in range(COLUMNS):
			pass_boxes.append([val] * ROWS)
		return pass_boxes
		