# domain/game_state.py
from typing import NamedTuple, Tuple
from .player import Player
from .platform import Platform
from .obstacle import Obstacle
from .powerup import PowerUp

class GameState(NamedTuple):
    player: Player
    platforms: Tuple[Platform, ...]
    obstacles: Tuple[Obstacle, ...]
    powerups: Tuple[PowerUp, ...]
    score: int
    is_running: bool
    is_game_over: bool

def create_initial_state(player: Player, platforms: Tuple[Platform, ...], obstacles: Tuple[Obstacle, ...], powerups: Tuple[PowerUp, ...]) -> GameState:
    return GameState(player, platforms, obstacles, powerups, 0, True, False)
