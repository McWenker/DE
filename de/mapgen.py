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
	def __init__(self):
		# sets all tiles to passable
		self.terrain = self.generate_map()
	
	def generate_map(self):
		# returns a map with all values set to 0
		game_map = []
		for i in range(ROWS):
			row = []
			for j in range(COLUMNS):
				x = 2*(perlin.noise2(i,j))
				if x >= -2 and x < -1.7:
					row.append(Tile(pos=(i,j), terrain='DeepWater'))
				elif x >= -1.7 and x < -1.2:
					row.append(Tile(pos=(i,j), terrain='ShalWater'))
				elif x >= -1.2 and x < -0.5:
					row.append(Tile(pos=(i,j), terrain='LowGrass'))
				elif x >= -0.5 and x < 0.3:
					row.append(Tile(pos=(i,j), terrain='HighGrass'))
				elif x >= 0.3 and x < 0.7:
					row.append(Tile(pos=(i,j), terrain='ShalDirt'))
				elif x >= 0.7 and x < 1.2:
					row.append(Tile(pos=(i,j), terrain='DeepDirt'))
				elif x >= 1.2 and x < 1.7:
					row.append(Tile(pos=(i,j), terrain='Rock'))
				elif x >= 1.7 and x < 2:
					row.append(Tile(pos=(i,j), terrain='Granite'))
			game_map.append(row)
		return game_map
		
	def get_passable_tiles(self, val):
		pass_boxes = []
		for i in range(COLUMNS):
			pass_boxes.append([val] * ROWS)
		return pass_boxes
		