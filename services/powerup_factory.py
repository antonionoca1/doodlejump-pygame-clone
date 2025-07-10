# services/powerup_factory.py
from domain.powerup import create_powerup, PowerUp
from domain.powerup_types import PowerUpType
import random
from typing import Tuple

def generate_powerups(count: int, y_start: float) -> Tuple[PowerUp, ...]:
    return tuple(
        create_powerup(
            random.uniform(0, 350),
            y_start - i * 400,
            random.choice([t.value for t in PowerUpType])
        ) for i in range(count)
    )
