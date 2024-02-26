import unittest
import tictactoe


class testTicTacToe(unittest.TestCase):
    def test(self):
        self.assertEqual(tictactoe.tictactoe(
            [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]), "A")
        self.assertEqual(tictactoe.tictactoe(
            [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]), "B")
        self.assertEqual(tictactoe.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [
                         1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]), "Draw")
        self.assertEqual(tictactoe.tictactoe([[0, 0], [2, 0]]), "Pending")


if __name__ == "__main__":
    unittest.main()
