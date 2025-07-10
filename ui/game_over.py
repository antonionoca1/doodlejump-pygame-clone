# ui/game_over.py
import pygame
from pygame.surface import Surface
from pygame.font import Font
from ui.debug_info import draw_debug_info

def wrap_text(text: str, font: Font, max_width: int) -> list[str]:
    words = text.split(' ')
    lines = []
    current = ''
    for word in words:
        test = f'{current} {word}'.strip()
        if font.size(test)[0] <= max_width:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def draw_game_over(screen: Surface, font: Font, score: int, high_score: int, clock: pygame.time.Clock) -> None:
    screen.fill((255, 255, 255))
    # Use a larger font for the title
    title_font = pygame.font.Font(None, 64)
    over_text = title_font.render('Game Over', True, (0, 0, 0))
    # Use a slightly larger font for other text
    menu_font = pygame.font.Font(None, 36)
    score_text = menu_font.render(f'Score: {score}', True, (0, 0, 0))
    high_score_text = menu_font.render(f'High Score: {high_score}', True, (0, 0, 0))
    screen.blit(over_text, (100, 80))
    screen.blit(score_text, (100, 160))
    screen.blit(high_score_text, (100, 210))
    instructions = [
        'Press R to restart the game.',
        'Press Esc to quit.'
    ]
    y = 280
    for text in instructions:
        for line in wrap_text(text, menu_font, 400):
            rendered = menu_font.render(line, True, (0, 0, 0))
            screen.blit(rendered, (60, y))
            y += 30  # Increased spacing
    draw_debug_info(screen, clock)
