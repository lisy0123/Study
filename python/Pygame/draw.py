import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 80, 80)
ORANGE = (255, 150, 50)
YELLOW = (255, 255, 150)
GREEN = (60, 255, 60)
PINK = (255, 80, 255)
BLUE = (90, 90, 255)
SKYBLUE = (80, 255, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

mousedown = False
mouseposition = []

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	elif event.type == pygame.MOUSEBUTTONDOWN:
		mousedown = True
		color = random.choice([RED, ORANGE, YELLOW, GREEN, PINK, SKYBLUE, BLUE, WHITE])
	elif event.type == pygame.MOUSEBUTTONUP:
		mousedown = False
		mouseposition.clear()
	elif event.type == pygame.MOUSEMOTION:
		if mousedown:
			mouseposition.append(event.pos)

	screen.fill(BLACK)

	if len(mouseposition) > 1:
		pygame.draw.lines(screen, color, False, mouseposition)

	pygame.display.update()
	clock.tick(50)

pygame.quit()
