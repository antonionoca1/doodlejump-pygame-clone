# domain/platform.py
from typing import NamedTuple

class Platform(NamedTuple):
    x: float
    y: float
    type: str
    is_active: bool

def create_platform(x: float, y: float, type: str) -> Platform:
    return Platform(x, y, type, True)

def deactivate_platform(platform: Platform) -> Platform:
    return platform._replace(is_active=False)
