import unittest
import pygame
from main import init_pygame
from ui.player import Player
from ui.platforms import PlatformManager

class TestMain(unittest.TestCase):
    def test_init_pygame(self):
        screen, clock = init_pygame()
        self.assertIsInstance(screen, pygame.Surface)
        self.assertIsInstance(clock, pygame.time.Clock)

    def test_player(self):
        player = Player(100, 500)
        self.assertEqual(player.rect.x, 100)
        self.assertEqual(player.rect.y, 500)
        self.assertFalse(player.is_game_over(600))
        player.rect.y = 601
        self.assertTrue(player.is_game_over(600))

    def test_platform_manager(self):
        pm = PlatformManager(400, 600)
        self.assertEqual(len(pm.platforms), 7)
        for plat in pm.platforms:
            self.assertIsInstance(plat, pygame.Rect)

if __name__ == "__main__":
    unittest.main()
