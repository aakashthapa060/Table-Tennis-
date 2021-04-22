import pygame


class Screen:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def screen_display(self):
		return pygame.display.set_mode((self.width,self.height))