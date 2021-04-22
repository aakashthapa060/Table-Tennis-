import pygame


class Enemy:
	enemyY_change = 0.5
	def __init__(self, enemyX,enemyY, enemyWidth,enemyHeight,screen):
		self.enemyX = enemyX
		self.enemyY = enemyY
		self.enemyWidth = enemyWidth
		self.enemyHeight = enemyHeight
		self.screen = screen

	def create_enemy(self):
		return pygame.draw.rect(self.screen, [0, 0, 0], [self.enemyX, self.enemyY, self.enemyWidth, self.enemyHeight])
	
	def enemy_move(self):
		self.enemyY += self.enemyY_change

		if self.enemyY < 0:
			self.enemyY_change = 0.5

		if self.enemyY >= (500 - self.enemyHeight):
			self.enemyY_change = -0.5
