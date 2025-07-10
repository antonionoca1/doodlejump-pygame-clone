# services/player_physics.py
from domain.player import Player

def apply_gravity(player: Player, gravity: float) -> Player:
    return player._replace(vy=player.vy + gravity)

def update_position(player: Player) -> Player:
    return player._replace(y=player.y + player.vy)
