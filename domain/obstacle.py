# domain/obstacle.py
from typing import NamedTuple

class Obstacle(NamedTuple):
    x: float
    y: float
    type: str
    is_active: bool

def create_obstacle(x: float, y: float, type: str) -> Obstacle:
    return Obstacle(x, y, type, True)

def deactivate_obstacle(obstacle: Obstacle) -> Obstacle:
    return obstacle._replace(is_active=False)
