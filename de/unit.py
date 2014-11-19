import pygame
from pygame.locals import *
from screen import Screen
from time import sleep
from util.vector2d import Vec2d
import math

screen = Screen()
pygame.init()

class Unit(pygame.sprite.Sprite):

	def __init__(self, color, width, height):

		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.width = width
		self.height = height
		self.speed = 10
		

		self.image = pygame.image.load('worker.png')

		self.rect = self.image.get_rect()
		self.currentpos = Vec2d([self.rect.x, self.rect.y])
		self.destination = Vec2d([0,0])

	def setDestination(self, dest):
		self.destination = Vec2d(dest)


	def updatePos(self):

		# Only move if the destination is different from our location
		if (Vec2d([self.rect[0],self.rect[1]]) != self.destination):
									
			difference = (self.destination - self.currentpos)
			norm = (self.destination - self.currentpos).normalized()
			endpos = self.currentpos + norm * self.speed
			
			# Are we going to overshoot our target? (Closer than one speed increement)
			if (difference.get_length() < self.speed):
				self.currentpos = self.destination
			else:
				self.currentpos = endpos

			self.rect.centerx = self.currentpos[0]

			self.rect.centery = (self.currentpos[1] - 16)

		


