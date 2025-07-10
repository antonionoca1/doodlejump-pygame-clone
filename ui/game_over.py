# ui/game_over.py
import pygame
from pygame.surface import Surface
from pygame.font import Font

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

def draw_game_over(screen: Surface, font: Font, score: int, high_score: int) -> None:
    screen.fill((255, 255, 255))
    over_text = font.render('Game Over', True, (0, 0, 0))
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    high_score_text = font.render(f'High Score: {high_score}', True, (0, 0, 0))
    screen.blit(over_text, (100, 100))
    screen.blit(score_text, (100, 150))
    screen.blit(high_score_text, (100, 200))
    instructions = [
        'Press R to restart the game.',
        'Press Esc to quit.'
    ]
    y = 260
    for text in instructions:
        for line in wrap_text(text, font, 280):
            rendered = font.render(line, True, (0, 0, 0))
            screen.blit(rendered, (60, y))
            y += 32
