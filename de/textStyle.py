import pygame
from pygame.locals import *

class TextStyle(object):

	# General Font Config

	def __init__(self):
		self.fontFace = 'Comic Sans MS'
		self.size = 18
		self.lineHeight = 24
		self.antiAliased = True

		pygame.font.init()
		self.reg = pygame.font.SysFont(self.fontFace, self.size)
		self.heavy = pygame.font.SysFont(self.fontFace, self.size, bold=True)

	def drawRegular(self, text, color):
		return self.reg.render(text, self.antiAliased, color)

	def drawBold(self, text, color):
		return self.heavy.render(text, self.antiAliased, color)

	