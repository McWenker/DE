import pygame
from pygame.locals import *
import constants
from textStyle import TextStyle

class ResourceManager(object):

	resources = {
		'adamantium': 10,
		'cobalt': 0,
		'lead': 0,
		'tungsten': 0,
		'seeds': 999,
		'antimatter': 5
	}

	def __init__(self):
		pygame.init()
		self.textStyle = TextStyle()

	def add(self, resource, amt):
		self.resources[resource] += amt

	def get(self, resource):
		return self.resources[resource]

	def drawResources(self):
		list = []
		for item in self.resources:
			list.append(self.textStyle.drawRegular(item + '  ' + str(self.resources[item]), constants.WHITE))
		return list
