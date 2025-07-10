# domain/powerup.py
from typing import NamedTuple

class PowerUp(NamedTuple):
    x: float
    y: float
    type: str
    is_active: bool

def create_powerup(x: float, y: float, type: str) -> PowerUp:
    return PowerUp(x, y, type, True)

def deactivate_powerup(powerup: PowerUp) -> PowerUp:
    return powerup._replace(is_active=False)
