import pygame
from pygame.surface import Surface
from domain.player import Player

def draw_player(screen: Surface, player: Player) -> None:
    pygame.draw.ellipse(screen, (0, 200, 0), (player.x, player.y, 30, 30))
