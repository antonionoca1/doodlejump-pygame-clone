# services/platform_factory.py
from domain.platform import create_platform, Platform
from domain.platform_types import PlatformType
from typing import Tuple
import random

def generate_platforms(count: int, y_start: float) -> Tuple[Platform, ...]:
    return tuple(
        create_platform(
            random.uniform(0, 350),
            y_start - i * 60,
            random.choice([t.value for t in PlatformType])
        ) for i in range(count)
    )
