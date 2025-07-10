# ui/hud.py
import pygame
from pygame.surface import Surface
from pygame.font import Font
from ui.debug_info import draw_debug_info

def draw_hud(screen: Surface, font: Font, score: int, powerups: tuple[str, ...], clock: pygame.time.Clock) -> None:
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    draw_debug_info(screen, clock)
