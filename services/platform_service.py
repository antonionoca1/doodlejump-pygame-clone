# services/platform_service.py
from domain.platform import Platform

def move_platform(platform: Platform, dx: float, dy: float) -> Platform:
    return platform._replace(x=platform.x + dx, y=platform.y + dy)
