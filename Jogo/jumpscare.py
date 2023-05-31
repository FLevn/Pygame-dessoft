import pygame
import time

class Jumpscare:
    def __init__(self):
        pygame.init()

        # tela
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("hehehe")

        # frames
        self.frame1 = pygame.image.load('assets/anim/jumpscare/jumpscare1.png').convert()
        self.frame1 = pygame.transform.smoothscale(self.frame1, self.screen.get_size())
        self.frame2 = pygame.image.load('assets/anim/jumpscare/jumpscare2.png').convert()
        self.frame2 = pygame.transform.smoothscale(self.frame2, self.screen.get_size())

        # variáveis
        self.jumpscare_time = 0.5  # duração de cada frame (em segundos)
        self.total_jumpscare_frames = 2
        self.current_frame = 0
        self.jumpscare_start_time = 0

    def run(self):
        # loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # verifica condição
            if self.current_frame < self.total_jumpscare_frames:
                if self.current_frame == 0:
                    self.jumpscare_start_time = time.time()  # início do jumpscare

                elapsed_time = time.time() - self.jumpscare_start_time

                if elapsed_time >= self.jumpscare_time:
                    self.current_frame += 1

            # Display
            self.screen.fill((0, 0, 0))
            if self.current_frame == 0:
                self.screen.blit(self.frame1, (0, 0))
            elif self.current_frame == 1:
                self.screen.blit(self.frame2, (0, 0))

            pygame.display.flip()

        pygame.quit()