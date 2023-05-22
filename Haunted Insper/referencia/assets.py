import pygame
import os
from config import player_WIDTH, player_HEIGHT, ghost_WIDTH, ghost_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
ghost_IMG = 'ghost_img'
ghost_IMG = 'ghost_img'
player_IMG = 'player_img'
player_IMG = 'player_img'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, '')).convert()
    assets[ghost_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
    assets[ghost_IMG] = pygame.transform.scale(assets[''], (ghost_WIDTH, ghost_HEIGHT))
    assets[player_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
    assets[player_IMG] = pygame.transform.scale(assets[''], (player_WIDTH, player_HEIGHT))
    return assets
