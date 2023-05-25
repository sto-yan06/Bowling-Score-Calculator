import unittest
from unittest.mock import patch
from main import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    @patch('random.randint')
    def test_play_game_auto(self, mock_randint):
        mock_randint.side_effect = [4, 6, 7, 7, 2, 10, 3, 6, 3, 6, 10, 9, 0, 9, 0, 10, 0, 10, 0, 10, 8, 8, 1, 5, 5, 6]
        score = self.game.play_game_auto()
        self.assertEqual(score, 145)

    @patch('random.randint')
    def test_play_game_auto_with_zero_score(self, mock_randint):
        mock_randint.side_effect = [0] * 20
        score = self.game.play_game_auto()
        self.assertEqual(score, 0)

    @patch('random.randint')
    def test_play_game_auto_with_perfect_score(self, mock_randint):
        mock_randint.side_effect = [10] * 20
        score = self.game.play_game_auto()
        self.assertEqual(score, 300)

    @patch('random.randint')
    def test_play_game_auto_with_all_spares(self, mock_randint):
        mock_randint.side_effect = [5, 5] * 23 + [5]
        score = self.game.play_game_auto()
        self.assertEqual(score, 150)

if __name__ == '__main__':
    unittest.main()
