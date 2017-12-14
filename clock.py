import pygame
import datetime

pygame.init()
caption = 'Clock'
width = 300
height = 300
thickness = 0
area = width * height
DISPLAY = pygame.display.set_mode((width, height), 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
done = False
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.version.ver = '1.0.0'
pygame.display.set_caption(caption)
while not done:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	DISPLAY.fill(WHITE)
	pygame.draw.circle(DISPLAY, YELLOW, (width/2, height/2), 100, thickness)
	time = datetime.datetime.now().time()
	timeStrOld = str(time)
	timeStrNew = timeStrOld[0:3]+timeStrOld[3:6]+timeStrOld[6:8]
	textsurface = myfont.render(timeStrNew, False, BLUE)
	pygame.time.delay(999)
	DISPLAY.blit(textsurface, (DISPLAY.get_width()/2 - 40, DISPLAY.get_height()/2 - 5))
	pygame.display.update()
