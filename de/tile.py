import pygame
from constants import *
from pygame.locals import *

class Tile(object):
	def __init__(self, pos, sprite=None, terrain='Rock'):
		self.pos=pos
		self.sprite=sprite
		self.terrain=terrain
		self.rect=pygame.rect.Rect(pos[0],pos[1],TILE_SIZE,TILE_SIZE)