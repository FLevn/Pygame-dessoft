import pygame, sys
from config import *
from level import Level
from init_screen import init_screen

class Game:
	def __init__(self):
		  
		# setup geral
		pygame.init()
		
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Haunted Insper')
		self.clock = pygame.time.Clock()
		
		self.level = Level()
	
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

if __name__ == '__main__':
	game = Game()
	game.run()