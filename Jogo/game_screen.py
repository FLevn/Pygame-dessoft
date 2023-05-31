import pygame, sys
from pygame.locals import *
from config import *
from level import Level
from timer import Timer
from player import Player
pygame.mixer.init()
pygame.mixer.music.load('assets/Sons/trilha sonora do jogo.mp3')
pygame.mixer.music.set_volume(3)
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
		countframes=0
		tempo=0
		while True:
			countframes+=1
			if countframes>=FPS:
				tempo+=1
				countframes=0
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			font = pygame.font.Font(None,36)
			showtime=font.render('tempo:  '+str(tempo),True,WHITE)
			self.screen.blit(showtime,(200,10))
			pygame.display.update()
			self.clock.tick(FPS)
			self.timer.update()
			
if __name__ == '__main__':
	game = Game()
	game.run()