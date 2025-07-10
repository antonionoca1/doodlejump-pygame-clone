# main.py
import pygame
from pygame.surface import Surface
from pygame.font import Font
from typing import Any
from domain.player import create_player, Player
from domain.platform import create_platform, Platform
from domain.obstacle import Obstacle
from domain.powerup import PowerUp
from domain.game_state import create_initial_state, GameState
from services.platform_factory import generate_platforms
from services.obstacle_factory import generate_obstacles
from services.powerup_factory import generate_powerups
from services.player_service import move_player
from services.game_logic import handle_platform_collision, handle_obstacle_collision, handle_powerup_collision
from services.collision_service import check_platform_collision, check_obstacle_collision, check_powerup_collision
from services.player_physics import apply_gravity, update_position
from ui.main_menu import draw_main_menu
from ui.hud import draw_hud
from ui.game_over import draw_game_over
from ui.high_scores import draw_high_scores
from ui.player import draw_player
from ui.platforms import draw_platforms

def process_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def get_horizontal_input() -> int:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        return -5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        return 5
    return 0

def update_vertical_scroll(player: Player, state: GameState, scroll_y: float) -> tuple[Player, GameState, float]:
    if player.y < 250:
        scroll = 250 - player.y
        player = player._replace(y=250)
        platforms = tuple(p._replace(y=p.y + scroll) for p in state.platforms)
        obstacles = tuple(o._replace(y=o.y + scroll) for o in state.obstacles)
        powerups = tuple(pu._replace(y=pu.y + scroll) for pu in state.powerups)
        state = state._replace(platforms=platforms, obstacles=obstacles, powerups=powerups)
        scroll_y += scroll
    return player, state, scroll_y

def generate_new_platforms(state: GameState) -> GameState:
    highest_platform_y = min(p.y for p in state.platforms)
    platforms = state.platforms
    while highest_platform_y > 0:
        new_platforms = generate_platforms(3, highest_platform_y)
        platforms += new_platforms
        highest_platform_y = min(p.y for p in platforms)
    return state._replace(platforms=platforms)

def remove_offscreen_platforms(state: GameState) -> GameState:
    return state._replace(platforms=tuple(p for p in state.platforms if p.y < 600))

def check_player_fall(player: Player, state: GameState) -> GameState:
    if player.y > 600:
        return state._replace(is_game_over=True)
    return state

def game_loop(screen: Surface, font: Font) -> int:
    state, player, scroll_y, clock, running = init_game_state()
    while running and not state.is_game_over:
        state, player, scroll_y, running = game_tick(state, player, scroll_y, screen, font, clock)
    show_game_over(screen, font, state)
    return state.score


def init_game_state() -> tuple[GameState, Player, float, pygame.time.Clock, bool]:
    player = create_player(200, 500)
    start_platform = create_platform(player.x, player.y + 28, 'normal')
    platforms = (start_platform,) + generate_platforms(9, 600)
    obstacles = generate_obstacles(2, 600)
    powerups = generate_powerups(1, 600)
    state = create_initial_state(player, platforms, obstacles, powerups)
    return state, player, 0, pygame.time.Clock(), True


def game_tick(state: GameState, player: Player, scroll_y: float, screen: Surface, font: Font, clock: pygame.time.Clock) -> tuple[GameState, Player, float, bool]:
    running = process_events()
    dx = get_horizontal_input()
    player = move_player(state.player, dx)
    player = apply_gravity(player, 0.5)
    player = update_position(player)
    player, state, scroll_y = update_vertical_scroll(player, state, scroll_y)
    state, player = handle_collisions(state, player, scroll_y)
    state = generate_new_platforms(state)
    state = remove_offscreen_platforms(state)
    state = check_player_fall(player, state)
    render_game(screen, font, state, player, scroll_y)
    clock.tick(60)
    return state, player, scroll_y, running


def handle_collisions(state: GameState, player: Player, scroll_y: float) -> tuple[GameState, Player]:
    idx = check_platform_collision(player, state.platforms)
    if idx is not None:
        player = player._replace(vy=-15)
        state = state._replace(player=player)
        state = handle_platform_collision(state, idx)
        state = state._replace(score=state.score + 10)
    idx = check_obstacle_collision(player, state.obstacles)
    if idx is not None:
        state = handle_obstacle_collision(state, idx)
    idx = check_powerup_collision(player, state.powerups)
    if idx is not None:
        state = handle_powerup_collision(state, idx)
    state = state._replace(player=player)
    return state, player


def render_game(screen: Surface, font: Font, state: GameState, player: Player, scroll_y: float) -> None:
    screen.fill((255, 255, 255))
    draw_platforms(screen, state.platforms)
    draw_player(screen, player)
    draw_hud(screen, font, state.score + int(scroll_y), state.player.powerups)
    pygame.display.flip()


def show_game_over(screen: Surface, font: Font, state: GameState) -> None:
    draw_game_over(screen, font, state.score, state.score)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def main() -> None:
    pygame.init()
    screen: Surface = pygame.display.set_mode((400, 600))
    font: Font = pygame.font.SysFont('Arial', 32)
    while True:
        draw_main_menu(screen, font)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                score = game_loop(screen, font)
                draw_game_over(screen, font, score, score)
                pygame.display.flip()
                pygame.time.wait(2000)
                break

if __name__ == '__main__':
    main()
