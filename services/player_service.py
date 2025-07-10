# services/player_service.py
from domain.player import Player

def move_player(player: Player, dx: float) -> Player:
    return player._replace(x=player.x + dx)

def jump_player(player: Player, vy: float) -> Player:
    return player._replace(vy=vy)
