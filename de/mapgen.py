import pygame, math, sys, random
<<<<<<< HEAD
from util.perlin import SimplexNoise
=======
>>>>>>> 4ef4cb7fa0098cab22df57d2ea869a4a0870fd90
from pygame.locals import *
from random import randint, choice
from constants import *
from tile import Tile

<<<<<<< HEAD
perlin = SimplexNoise(period=500)

=======
>>>>>>> 4ef4cb7fa0098cab22df57d2ea869a4a0870fd90
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
<<<<<<< HEAD
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
=======
				x = randint(0,4)
				if x == 0:
					row.append(Tile(pos=(i,j), terrain='Dirt'))
				elif x == 1:
					row.append(Tile(pos=(i,j), terrain='Grass'))
				elif x == 2:
					row.append(Tile(pos=(i,j), terrain='Water'))
				else:
					row.append(Tile(pos=(i,j), terrain='Rock'))
>>>>>>> 4ef4cb7fa0098cab22df57d2ea869a4a0870fd90
			game_map.append(row)
		return game_map
		
	def get_passable_tiles(self, val):
		pass_boxes = []
		for i in range(COLUMNS):
			pass_boxes.append([val] * ROWS)
		return pass_boxes
		