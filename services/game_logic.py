# services/game_logic.py
from domain.game_state import GameState
from domain.player import Player
from domain.platform import Platform
from domain.obstacle import Obstacle
from domain.powerup import PowerUp

def update_game_state(state: GameState, input_dir: int) -> GameState:
    # ...existing code...
    # (Stub for main game update loop)
    return state

def handle_platform_collision(state: GameState, idx: int) -> GameState:
    # Do not deactivate platforms after collision
    return state

def handle_obstacle_collision(state: GameState, idx: int) -> GameState:
    player = state.player._replace(is_alive=False)
    return state._replace(player=player, is_game_over=True)

def handle_powerup_collision(state: GameState, idx: int) -> GameState:
    powerups = tuple(
        pu._replace(is_active=False) if i == idx else pu
        for i, pu in enumerate(state.powerups)
    )
    return state._replace(powerups=powerups)
