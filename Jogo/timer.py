import pygame
import time

class Timer:
    def __init__(self, screen, font, position=(10, 10), color=(255, 255, 255)):
        self.screen = screen
        self.font = font
        self.position = position
        self.color = color
        self.start_time = time.time()

    def update(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_text = f"Time: {minutes:02d}:{seconds:02d}"

        text_surface = self.font.render(timer_text, True, self.color)
        self.screen.blit(text_surface, self.position)