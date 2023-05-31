import pygame, sys
from config import *
from level import Level
from init_screen import init_screen
from timer import Timer
pygame.mixer.init()
pygame.mixer.music.load('assets/Sons/trilha.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)


class Game:
	def __init__(self):
		  
		# setup geral
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Haunted Insper')
		self.clock = pygame.time.Clock()

		self.level = Level()

		self.timer = Timer(self.screen)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			self.timer.update()

if __name__ == '__main__':
	game = Game()
	game.run()