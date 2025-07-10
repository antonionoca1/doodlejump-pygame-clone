# services/obstacle_factory.py
from domain.obstacle import create_obstacle, Obstacle
from domain.obstacle_types import ObstacleType
import random
from typing import Tuple

def generate_obstacles(count: int, y_start: float) -> Tuple[Obstacle, ...]:
    return tuple(
        create_obstacle(
            random.uniform(0, 350),
            y_start - i * 200,
            random.choice([t.value for t in ObstacleType])
        ) for i in range(count)
    )
