import pygame
from pygame.locals import *

class Tile(object):
	def __init__(self, pos, sprite=None, type='passable'):
		self.pos=pos
		self.sprite=sprite
		self.type=type
		self.rect=pygame.rect.Rect(pos[0],pos[1],32,32)