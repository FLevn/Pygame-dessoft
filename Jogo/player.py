import pygame 
from config import *
from support import import_folder
from entity import Entity
from jumpscare import Jumpscare

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack):
		super().__init__(groups)
		self.image = pygame.image.load('assets/img/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)

		# gráficos
		self.import_player_assets()
		self.status = 'down'

		# movimento
		self.direction = pygame.math.Vector2()
		self.speed = 5
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites

		self.health = 90

		# flashlight
		self.create_attack = create_attack
		self.destroy_attack = destroy_attack

		self.vulnerable = True
		self.hurt_time = None
		self.invulnerability_duration = 500

		self.obstacle_sprites = obstacle_sprites

	def import_player_assets(self):
		character_path = 'assets/anim/player/'
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			# movimentação
			if keys[pygame.K_UP] or keys[pygame.K_w]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

			# lanterna
			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()


	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle','_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack','')

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
				self.destroy_attack()
		
		if not self.vulnerable:
			if current_time - self.hurt_time >= self.invulnerability_duration:
				self.vulnerable = True
				self.health -= 30

	def animate(self):
		animation = self.animations[self.status]

		# índice do frame 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# imagem
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

	def check_death(self):
		if self.health <= 0:
			self.kill()
			jumpscare = Jumpscare()
			jumpscare.run()
				

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)
		self.check_death()