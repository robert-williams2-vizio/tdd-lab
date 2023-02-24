from unittest import TestCase

# from src import Game 

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