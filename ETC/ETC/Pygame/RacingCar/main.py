import pygame
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GAY = (150, 150, 150)
RED = (255, 0, 0)

class Car:
	image_car = ['pic/RacingCar01.png', 'pic/RacingCar02.png', 'pic/RacingCar03.png', 'pic/RacingCar04.png', 'pic/RacingCar05.png', \
					'pic/RacingCar06.png', 'pic/RacingCar07.png', 'pic/RacingCar08.png', 'pic/RacingCar09.png', 'pic/RacingCar10.png', \
					'pic/RacingCar11.png', 'pic/RacingCar12.png', 'pic/RacingCar13.png', 'pic/RacingCar14.png', 'pic/RacingCar15.png', \
					'pic/RacingCar16.png', 'pic/RacingCar17.png', 'pic/RacingCar18.png', 'pic/RacingCar19.png', 'pic/RacingCar20.png']
	def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
		self.image = ""
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

	def load_image(self):
		self.image = pygame.image.load(random.choice(self.image_car))
		self.width = self.image.get_rect().size[0]
		self.height = self.image.get_rect().size[1]

	def draw_image(self):
		screen.blit(self.image, [self.x, self.y])

	def move_x(self):
		self.x += self.dx

	def move_y(self):
		self.y += self.dy

	def check_out_of_screen(self):
		if self.x + self.width > WINDOW_WIDTH or self.x < 0:
			self.x -= self.dx
		if self.y + self.height > WINDOW_HEIGHT or self.y < 0:
			self.y -= self.dy

	def check_crash(self, car):
		if (self.x + self.width > car.x) and (self.x < car.x + car.width) and (self.y < car.y + car.height) and (self.y + self.height > car.y):
			return True
		else:
			return False

def draw_main_menu():
	draw_x = (WINDOW_WIDTH / 2) - 200
	draw_y = WINDOW_HEIGHT / 2
	image_intro = pygame.image.load('pic/Car.png')
	screen.blit(image_intro, [draw_x, draw_y - 280])
	font_40 = pygame.font.SysFont("FixedSys", 40, True, False)
	font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
	text_title = font_40.render("Racing Car Game", True, BLACK)
	screen.blit(text_title, [draw_x, draw_y])
	text_score = font_40.render("Score: " + str(score), True, WHITE)
	screen.blit(text_score, [draw_x, draw_y + 70])
	text_start = font_40.render("Press Space Key to Start!", True, RED)
	screen.blit(text_start, [draw_x, draw_y + 140])
	pygame.display.flip()

def draw_score():
	font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
	text_score = font_30.render("Score: " + str(score), True, BLACK)
	screen.blit(text_score, [15, 15])

if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption("RacingCar")
	clock = pygame.time.Clock()

	pygame.mixer.music.load('pic/race.wav')
	sound_crash = pygame.mixer.Sound('pic/crash.wav')
	sound_engine = pygame.mixer.Sound('pic/engine.wav')

	player = Car(WINDOW_WIDTH / 3, WINDOW_HEIGHT - 150, 0, 0)
	player.load_image()

	cars = []
	car_count = 3
	for i in range(car_count):
		x = random.randrange(0, WINDOW_WIDTH - 55)
		y = random.randrange(-150, -50)
		car = Car(x, y, 0, random.randint(5,13))
		car.load_image()
		cars.append(car)

	lines = []
	line_width = 10
	line_height = 80
	line_margin = 20
	line_count = 20
	line_x = (WINDOW_WIDTH - line_width) / 2
	line_y = -10
	for i in range(line_count):
		lines.append([line_x, line_y])
		line_y +=line_height + line_margin

	score = 0
	crash = True
	game_on = True
	while game_on:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_on = False

			if crash:
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					crash = False
					for i in range(car_count):
						cars[i].x = random.randrange(0, WINDOW_WIDTH - cars[i].width)
						cars[i].y = random.randrange(-150, -50)
						cars[i].load_image()

					player.load_image()
					player.x = WINDOW_WIDTH / 2
					player.y = 650
					player.dx = 0
					player.dy = 0
					score = 0
					pygame.mouse.set_visible(False)
					sound_engine.play()
					sleep(5)
					pygame.mixer.music.play(-1)

			if not crash:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						player.dx = 8
					elif event.key == pygame.K_LEFT:
						player.dx = -8
					elif event.key == pygame.K_UP:
						player.dy = -8
					elif event.key == pygame.K_DOWN:
						player.dy = 8
			
				if  event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						player.dx = 0
					elif event.key == pygame.K_LEFT:
						player.dx = 0
					elif event.key == pygame.K_UP:
						player.dy = 0
					elif event.key == pygame.K_DOWN:
						player.dy = 0

		screen.fill(GAY)

		if not crash:
			for i in range(line_count):
				pygame.draw.rect(screen, WHITE, [lines[i][0], lines[i][1], line_width, line_height])
				lines[i][1] += 10
				if lines[i][1] > WINDOW_HEIGHT:
					lines[i][1] = -40 - line_height

			player.draw_image()
			player.move_x()
			player.move_y()
			player.check_out_of_screen()

			for i in range(car_count):
				cars[i].draw_image()
				cars[i].y += cars[i].dy
				if cars[i].y > WINDOW_HEIGHT:
					score += 10
					cars[i].x = random.randrange(0, WINDOW_HEIGHT - cars[i].width)
					cars[i].y = random.randrange(-150, -50)
					cars[i].dy = random.randrange(5, 13)
					cars[i].load_image()

			for i in range(car_count):
				if player.check_crash(cars[i]):
					crash = True
					pygame.mixer.music.stop()
					sound_crash.play()
					sleep(2)
					pygame.mouse.set_visible(True)
					break

			draw_score()
			pygame.display.flip()

		else:
			draw_main_menu()

		clock.tick(60)

	pygame.quit()
