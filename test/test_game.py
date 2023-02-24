from unittest import TestCase

from src import Game 

'''
Game
    - roll(int) -> None
    - score() -> int
'''

class GameTest(TestCase):

    def setUp(self) -> None:
        self.Game = Game.Game()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        pass

    def test_roll_20times_0(self):
        for x in range(20):
            self.Game.roll(0)

        self.assertEqual(self.Game.score(), 0)