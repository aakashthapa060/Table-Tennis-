import pygame


class Player:
	playerY_change = 0.5
	def __init__(self, playerX,playerY, playerWidth,playerHeight,screen):
		self.playerX = playerX
		self.playerY = playerY
		self.playerWidth = playerWidth
		self.playerHeight = playerHeight
		
		self.screen = screen
	def create_player(self):
		return pygame.draw.rect(self.screen, [0, 0, 0], [self.playerX, self.playerY, self.playerWidth, self.playerHeight])


	

	def player_move(self):
		self.playerY += self.playerY_change

		if self.playerY < 0:
			self.playerY_change = 0.5

		if self.playerY >= (500 - self.playerHeight):
			self.playerY_change = -0.5