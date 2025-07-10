# services/collision_service.py
from domain.player import Player
from domain.platform import Platform
from domain.obstacle import Obstacle
from domain.powerup import PowerUp

def check_platform_collision(player: Player, platforms: tuple[Platform, ...]) -> int | None:
    for i, p in enumerate(platforms):
        if abs(player.x - p.x) < 40 and abs(player.y - p.y) < 10 and p.is_active:
            return i
    return None

def check_obstacle_collision(player: Player, obstacles: tuple[Obstacle, ...]) -> int | None:
    for i, o in enumerate(obstacles):
        if abs(player.x - o.x) < 40 and abs(player.y - o.y) < 10 and o.is_active:
            return i
    return None

def check_powerup_collision(player: Player, powerups: tuple[PowerUp, ...]) -> int | None:
    for i, pu in enumerate(powerups):
        if abs(player.x - pu.x) < 40 and abs(player.y - pu.y) < 10 and pu.is_active:
            return i
    return None
