# ui/main_menu.py
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

def draw_main_menu(screen: Surface, font: Font) -> None:
    screen.fill((255, 255, 255))
    title = font.render('Doodle Jump', True, (0, 0, 0))
    screen.blit(title, (100, 100))
    controls = [
        'Controls:',
        'Left/Right Arrow or A/D: Move',
        'Enter: Start Game',
        'R: Restart (in game over screen)',
        'Esc: Quit'
    ]
    y = 180
    for text in controls:
        for line in wrap_text(text, font, 280):
            rendered = font.render(line, True, (0, 0, 0))
            screen.blit(rendered, (60, y))
            y += 32
