import pygame
import os
import psutil
from pygame.surface import Surface
from pygame.font import Font

def draw_debug_info(screen: Surface, clock: pygame.time.Clock) -> None:
    font = pygame.font.Font(None, 12)
    fps = clock.get_fps()
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    text = f"FPS: {fps:.1f}  MEM: {mem_mb:.1f}MB"
    rendered = font.render(text, True, (50, 50, 50))
    w, _ = screen.get_size()
    screen.blit(rendered, (w - rendered.get_width() - 10, 10))
