import random
from os import path

import pygame
from config import BLACK, FPS, GAME, GIF_DIR, QUIT,HEIGTH, WIDTH
WHITE=(255,255,255)

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(GIF_DIR, 'Tela_inicial.gif')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def start_screen():
    screen=pygame.display.set_mode(1280,720)
    pygame.display.set.caption('game title')
    screen.fill(BLACK)
    
    # Display title text
    font = pygame.font.Font(None, 48)
    text = font.render("Game Title", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGTH // 2 - 50))
    screen.blit(text, text_rect)
    
    # Display play button
    play_button = pygame.Rect(WIDTH // 2 - 75, HEIGTH // 2 + 50, 150, 50)
    pygame.draw.rect(screen, WHITE, play_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button.center)
    screen.blit(text, text_rect)
    
    pygame.display.flip()