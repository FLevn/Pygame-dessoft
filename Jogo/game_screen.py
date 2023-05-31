import pygame, sys
from config import *
from level import Level
from init_screen import init_screen
from init_screen import *
start_screen=True

class Game:
	def __init__(self):
		  
		# setup geral
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Haunted Insper')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		play_button = pygame.Rect(WIDTH // 2 - 75, HEIGTH // 2 + 50, 150, 50)

		while True:
			if startscreen:
				start_screen()
			for event in pygame.event.get():


				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.SPACE:
					if event.button == 1:
						mouse_pos = pygame.mouse.get_pos()
						if play_button.collidepoint(mouse_pos):
							# Start the game or transition to the next screen
							startscreen = False
			else:
				self.screen.fill('black')
				self.level.run()
				pygame.display.update()
				self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()