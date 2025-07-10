import pygame
from pygame.surface import Surface
from domain.platform import Platform
from typing import Tuple

def draw_platforms(screen: Surface, platforms: Tuple[Platform, ...]) -> None:
    for p in platforms:
        color = (100, 100, 100) if p.is_active else (200, 200, 200)
        pygame.draw.rect(screen, color, (p.x, p.y, 60, 10))
