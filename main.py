import pygame,random,math
from screen import Screen
from player import Player
from enemy import Enemy

# Pygame initilaize
pygame.init()

#Game Screen
screenWidth = 800
screenHeight = 500
window = Screen(screenWidth,screenHeight)
screen = window.screen_display()

# Title and Logo
pygame.display.set_caption("ShootBhoot")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Player
playerX = 10

playerY = 10
playerY_change = 200
playerWidth = 15
playerHeight = 50
playerScore = 0
player = Player(playerX,playerY,playerWidth,playerHeight,screen)

#Enemy
enemyWidth = 15 
enemyHeight = 50
enemyX = screenWidth - (enemyWidth + 10)
enemyY = 10
enemyScore = 0
enemy = Enemy(enemyX,enemyY,enemyWidth,enemyHeight,screen)

# Ball
ballRadius = 10
ballX = random.randint(0, screenWidth - 10)
ballY = random.randint(0, screenHeight - 10)
ballSpeed = 0.4
ballX_change = ballSpeed
ballY_change = ballSpeed
def ball_create(screen, ballX, ballY, radius):
	return pygame.draw.circle(screen, (10, 10, 10), (ballX, ballY), radius)


def distance(playerX,playerY,ballX,ballY):
	calc = math.sqrt((playerX - ballX)**2 + (playerY - ballY)**2)
	return calc
# Font
WinOrLose = "Table Tennis"
font = pygame.font.Font('nexa.otf', 32)
def ScoreBoard():
	text = font.render(WinOrLose, True, (255,255,255), (0,0,0))
	textRect = text.get_rect()
	textRect.center = (screenWidth // 2,  20)
	screen.blit(text, textRect)
#Player Score
def player_socre():
	playerText = font.render(str(playerScore)+ "", True, (255,255,255), (0,0,0))
	playerTextRect = playerText.get_rect()
	playerTextRect.center = (screenWidth // 2 - 40,  60)
	screen.blit(playerText, playerTextRect)
#Enemy Score
def enemy_score():
	enemyText = font.render(str(enemyScore)+ "", True, (255,255,255), (0,0,0))
	enemyTextRect = enemyText.get_rect()
	enemyTextRect.center = (screenWidth // 2 + 40,  60)
	screen.blit(enemyText, enemyTextRect)

#Game loop
running = True

while running:
	screen.fill((255,255,255))
	ScoreBoard()
	player_socre()
	enemy_score()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.playerY_change = -0.5

			if event.key == pygame.K_DOWN:
				player.playerY_change = 0.5

			if event.key == pygame.K_w:
				enemy.enemyY_change = -0.5

			if event.key == pygame.K_s:
				enemy.enemyY_change = 0.5



	

	# Player Move 
	player.player_move()

	# Ball Moving
	ballX -= ballX_change
	ballY -= ballY_change
	P_a_B = distance(player.playerX, player.playerY, ballX,ballY)
	E_a_B = distance(enemy.enemyX, enemy.enemyY, ballX,ballY)

	if ballY <= 0:
		ballY_change = -ballSpeed
	elif ballY >= (screenHeight - ballRadius):
		ballY_change = ballSpeed
	if ballX < -50:
		enemyScore += 1
		ballX = random.randint(300,400)
	elif ballX > 850:
		playerScore += 1
		ballX = ballX = random.randint(100,200)



	if P_a_B <= 30:
		ballX_change = -ballSpeed

	if E_a_B <= 30:
		ballX_change = ballSpeed

	if playerScore > 3 or enemyScore > 3:
		ballSpeed =0.5
	# Score BordChanger
	if enemyScore == 10:
		WinOrLose = "Player 2 Win"
	elif playerScore == 10:
		WinOrLose = "Player 1 Win"
		
	#Enemy
	enemy.enemy_move()

	enemy.create_enemy()
	ball_create(screen, ballX, ballY, ballRadius)
	player.create_player()
	pygame.display.flip()
	

	pygame.display.update()