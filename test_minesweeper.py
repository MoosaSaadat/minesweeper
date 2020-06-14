import unittest
import minesweeper as ms

class TestMinesweeper(unittest.TestCase):

    def test_mark_mine(self):
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 2)

        # First Cell
        sentence.mark_mine((0,1))
        self.assertEqual({(0,2), (0,3)}, sentence.cells)

        # Second Cell
        sentence.mark_mine((0,2))
        self.assertEqual({(0,3)}, sentence.cells)

        # Cell NOT in sentence
        sentence.mark_mine((2,1))
        self.assertEqual({(0,3)}, sentence.cells)

        # Check mine count
        self.assertEqual(0, sentence.count)


if __name__ == "__main__":
    unittest.main()