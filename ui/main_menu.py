# ui/main_menu.py
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

def draw_main_menu(screen: Surface, font: Font, clock: pygame.time.Clock) -> None:
    screen.fill((255, 255, 255))
    # Use a larger font for the title
    title_font = pygame.font.Font(None, 64)
    title = title_font.render('Doodle Jump', True, (0, 0, 0))
    screen.blit(title, (100, 80))
    # Use a slightly larger font for menu text
    menu_font = pygame.font.Font(None, 36)
    controls = [
        'Controls:',
        'Left/Right Arrow or A/D: Move',
        'Enter: Start Game',
        'R: Restart (in game over screen)',
        'Esc: Quit'
    ]
    y = 180
    for text in controls:
        for line in wrap_text(text, menu_font, 280):
            rendered = menu_font.render(line, True, (0, 0, 0))
            screen.blit(rendered, (60, y))
            y += 30  # Increased spacing
    draw_debug_info(screen, clock)
