import pygame
import random
from constants import *

class Bullet(pygame.sprite.Sprite):
	# BULLET BILL
	def __init__(self, shape, x, y):
		# call parent
		super(Bullet, self).__init__()

		self.shape = shape
		self.image = self.get_shape(self.shape)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def get_shape(self, shape):
		return pygame.image.load(IMG_DIR + 'arrah '+shape+'.png')
		

	def move(self):
		if self.x_speed > 0:
			self.rect.x += 3
		if self.x_speed < 0:
			self.rect.x -= 3
		if self.y_speed > 0:
			self.rect.y -= 3
		if self.y_speed < 0:
			self.rect.y += 3

	def fire(self, x_speed, y_speed):
		self.x_speed = x_speed
		self.y_speed = y_speed