# domain/platform_types.py
from enum import Enum

class PlatformType(Enum):
    NORMAL = 'normal'
    MOVING = 'moving'
    BREAKING = 'breaking'
    SPRING = 'spring'
