# domain/player.py
from typing import NamedTuple

class Player(NamedTuple):
    x: float
    y: float
    vy: float
    score: int
    is_alive: bool
    powerups: tuple

def create_player(x: float, y: float) -> Player:
    return Player(x, y, 0.0, 0, True, ())

def update_player_score(player: Player, delta: int) -> Player:
    return player._replace(score=player.score + delta)

def set_player_alive(player: Player, alive: bool) -> Player:
    return player._replace(is_alive=alive)
