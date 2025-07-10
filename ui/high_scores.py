# ui/high_scores.py
import pygame
from pygame.surface import Surface
from pygame.font import Font
from ui.debug_info import draw_debug_info

def draw_high_scores(screen: Surface, font: Font, scores: list[int], clock: pygame.time.Clock) -> None:
    screen.fill((255, 255, 255))
    title = font.render('High Scores', True, (0, 0, 0))
    screen.blit(title, (100, 100))
    for i, score in enumerate(scores):
        score_text = font.render(f'{i+1}. {score}', True, (0, 0, 0))
        screen.blit(score_text, (100, 150 + i * 30))
    draw_debug_info(screen, clock)
