import pygame
import random
import sys
from time import sleep

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640
rockImage = ['pic/rock01.png', 'pic/rock02.png', 'pic/rock03.png', 'pic/rock04.png', 'pic/rock05.png', \
		  'pic/rock06.png', 'pic/rock07.png', 'pic/rock08.png', 'pic/rock09.png', 'pic/rock10.png', \
		  'pic/rock11.png', 'pic/rock12.png', 'pic/rock13.png', 'pic/rock14.png', 'pic/rock15.png', \
		  'pic/rock16.png', 'pic/rock17.png', 'pic/rock18.png', 'pic/rock19.png', 'pic/rock20.png', \
		  'pic/rock21.png', 'pic/rock22.png', 'pic/rock23.png', 'pic/rock24.png', 'pic/rock25.png', \
		  'pic/rock26.png', 'pic/rock27.png', 'pic/rock28.png', 'pic/rock29.png', 'pic/rock30.png', ]
explosionSound = ['pic/explosion01.wav', 'pic/explosion02.wav', 'pic/explosion03.wav', 'pic/explosion04.wav']


def writeScore(count):
	global gamePad
	font = pygame.font.Font('pic/NanumGothic.ttf', 20)
	text = font.render('count: ' + str(count), True, (255, 255, 255))
	gamePad.blit(text, (10, 0))

def writePassed(count):
	global gamePad
	font = pygame.font.Font('pic/NanumGothic.ttf', 20)
	text = font.render('miss: ' + str(count), True, (255, 0, 0))
	gamePad.blit(text, (400, 0))

def writeMessage(text):
	global gamePad, gameoverSound
	textfont = pygame.font.Font('pic/NanumGothic.ttf', 50)
	text = textfont.render(text, True, (255,0,0))
	textpos = text.get_rect()
	textpos.center = (padWidth/2, padHeight/2)
	gamePad.blit(text, textpos)

	pygame.display.update()
	pygame.mixer.music.stop()
	gameoverSound.play()
	sleep(2)
	pygame.mixer.music.play(-1)
	runGame()


def crash():
	global gamePad
	writeMessage('CRASH!')

def gameOver():
	global gamePad
	writeMessage('GAME OVER!')

def drawObject(obj, x, y):
	global gamePad
	gamePad.blit(obj, (x, y))


def initGame():
	global gamePad, clock, background, fighter, gun, explosion, gunSound, gameoverSound
	pygame.init()
	gamePad = pygame.display.set_mode((padWidth, padHeight))
	pygame.display.set_caption('Shooting')
	background = pygame.image.load('pic/background.png')
	fighter = pygame.image.load('pic/fighter.png')
	gun = pygame.image.load('pic/missile.png')
	explosion = pygame.image.load('pic/explosion.png')
	pygame.mixer.music.load('pic/music.wav')
	pygame.mixer.music.play(-1)
	gunSound = pygame.mixer.Sound('pic/missile.wav')
	gameoverSound = pygame.mixer.Sound('pic/gameover.wav')
	clock = pygame.time.Clock()


def runGame():
	global gamepad, clock, background, fighter, gun, explosion, gunSound, gameoverSound

	fighterSize = fighter.get_rect().size
	fighterWidth = fighterSize[0]
	fighterHeight = fighterSize[1]

	x = padWidth * 0.45
	y = padHeight * 0.9
	fighterX = 0
	gunXY = []

	rock = pygame.image.load(random.choice(rockImage))
	rockSize = rock.get_rect().size
	rockWidth = rockSize[0]
	rockHeight = rockSize[1]
	destroySound = pygame.mixer.Sound(random.choice(explosionSound))
	
	rockX = random.randrange(0, padWidth - rockWidth)
	rockY = 0
	rockSpeed = 3

	isShot = False
	shotCount = 0
	rockPassed = 0

	onGame = False
	while not onGame:
		for event in pygame.event.get():
			if event.type in [pygame.QUIT]:
				pygame.quit()
				sys.exit()

			if event.type in [pygame.KEYDOWN]:
				if event.key == pygame.K_LEFT:
					fighterX -= 5
				elif event.key == pygame.K_RIGHT:
					fighterX += 5
				elif event.key == pygame.K_SPACE:
					gunSound.play()
					gunX = x + fighterWidth/2 - 5
					gunY = y - fighterHeight + 30
					gunXY.append([gunX, gunY])

			if event.type in [pygame.KEYUP]:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					fighterX = 0

		drawObject(background, 0, 0)
		# gamePad.fill(BLACK)
		x += fighterX
		if x < 0:
			x = 0
		elif x > padWidth - fighterWidth:
			x = padWidth - fighterWidth

		if y < rockY + rockHeight:
			if (rockX > x and rockX < (x + fighterWidth)) or \
				((rockX + rockWidth) > x and (rockX + rockWidth) < (x + fighterWidth)):
				crash()
		drawObject(fighter, x, y)
		
		if len(gunXY) != 0:
			for i, bxy in enumerate(gunXY):
				bxy[1] -= 10
				gunXY[i][1] = bxy[1]
				if bxy[1] < rockY:
					if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
						gunXY.remove(bxy)
						isShot = True
						shotCount += 1
				if bxy[1] <= 0:
					try:
						gunXY.remove(bxy)
					except:
						pass
		if len(gunXY) != 0:
			for bx, by in gunXY:
				drawObject(gun, bx, by)

		writeScore(shotCount)
		rockY += rockSpeed

		if rockY > padHeight:
			rock = pygame.image.load(random.choice(rockImage))
			rockSize = rock.get_rect().size
			rockWidth = rockSize[0]
			rockHeight = rockSize[1]
			rockX = random.randrange(0, padWidth - rockWidth)
			rockY = 0
			rockPassed += 1

		if rockPassed == 3:
			gameOver()

		writePassed(rockPassed)
		
		if isShot:
			drawObject(explosion, rockX, rockY)
			destroySound.play()
			rock = pygame.image.load(random.choice(rockImage))
			rockSize = rock.get_rect().size
			rockWidth = rockSize[0]
			rockHeigth = rockSize[1]
			rockX = random.randrange(0, padWidth - rockWidth)
			rockY = 0
			destroySound = pygame.mixer.Sound(random.choice(explosionSound))
			isShot = False

			rockSpeed += 0.1
			if rockSpeed >= 10:
				rockSpeed = 10

		drawObject(rock, rockX, rockY)
		pygame.display.update()
		clock.tick(60)
		
	pygame.quit()

initGame()
runGame()
