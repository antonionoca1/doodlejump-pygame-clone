import pygame
import sys
import random

WIDTH, HEIGHT = 400, 600
FPS = 60


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vel_y = 0
        self.max_height = y
        self.total_ascended = 0

    def update(self, keys, platforms, offset=0):
        self.vel_y += 0.5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        self.rect.y += int(self.vel_y)
        for plat in platforms.platforms:
            if self.rect.colliderect(plat) and self.vel_y > 0:
                self.vel_y = -13
        self.max_height = min(self.max_height, self.rect.y)
        self.total_ascended += offset

    def get_score(self):
        return self.total_ascended

    def get_height(self):
        return HEIGHT - self.rect.y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 0), self.rect)

    def is_game_over(self, screen_height):
        return self.rect.y > screen_height


class PlatformManager:
    def __init__(self, width, height, player_rect=None):
        self.platforms = []
        # First platform just below the player
        if player_rect:
            self.platforms.append(pygame.Rect(player_rect.x, player_rect.y + player_rect.height + 5, 60, 10))
        # Remaining platforms
        for i in range(6):
            self.platforms.append(
                pygame.Rect(random.randint(0, width - 60), height - (i + 1) * 100, 60, 10)
            )
        self.width = width
        self.height = height

    def update(self, player):
        offset = 0
        if player.rect.y < self.height // 2:
            offset = self.height // 2 - player.rect.y
            player.rect.y = self.height // 2
            for plat in self.platforms:
                plat.y += offset
        self.platforms = [plat for plat in self.platforms if plat.y < self.height]
        while len(self.platforms) < 7:
            new_y = self.platforms[-1].y - 100
            self.platforms.append(
                pygame.Rect(random.randint(0, self.width - 60), new_y, 60, 10)
            )
        return offset

    def draw(self, screen):
        for plat in self.platforms:
            pygame.draw.rect(screen, (200, 200, 0), plat)


def draw_hud(screen, score, clock):
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    fps_text = font.render(f"FPS: {clock.get_fps():.1f}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 40))


def show_main_menu(screen):
    font = pygame.font.Font(None, 48)
    menu_text = font.render("Press Enter to Start", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(menu_text, (60, HEIGHT // 2 - 24))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True


def show_game_over(screen, score):
    font = pygame.font.Font(None, 48)
    over_text = font.render("Game Over", True, (200, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(over_text, (100, HEIGHT // 2 - 48))
    screen.blit(score_text, (100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)


def init_pygame():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT)), pygame.time.Clock()


def main():
    screen, clock = init_pygame()
    if not show_main_menu(screen):
        pygame.quit()
        sys.exit()
    player = Player(WIDTH // 2, HEIGHT - 100)
    platforms = PlatformManager(WIDTH, HEIGHT, player.rect)
    score = 0
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        offset = platforms.update(player)
        player.update(keys, platforms, offset)
        score = player.get_score()
        screen.fill((135, 206, 250))
        platforms.draw(screen)
        player.draw(screen)
        draw_hud(screen, score, clock)
        pygame.display.flip()
        if player.is_game_over(HEIGHT):
            running = False
    show_game_over(screen, score)
    pygame.quit()


if __name__ == "__main__":
    main()
