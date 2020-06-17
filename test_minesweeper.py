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

    def test_mark_safe(self):
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 2)

        # First Cell
        sentence.mark_safe((0,1))
        self.assertEqual({(0,2), (0,3)}, sentence.cells)

        # Second Cell
        sentence.mark_safe((0,2))
        self.assertEqual({(0,3)}, sentence.cells)

        # Cell NOT in sentence
        sentence.mark_safe((2,1))
        self.assertEqual({(0,3)}, sentence.cells)

        # Check mine count
        self.assertEqual(2, sentence.count)

    def test_known_mines(self):

        # All are mines
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 3)
        self.assertEqual({(0,1), (0,2), (0,3)}, sentence.known_mines())

        # Not known
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 2)
        self.assertIsNone(sentence.known_mines())

    def test_known_safes(self):

        # All are safe
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 0)
        self.assertEqual({(0,1), (0,2), (0,3)}, sentence.known_safes())

        # Not known
        sentence = ms.Sentence([(0,1), (0,2), (0,3)], 2)
        self.assertIsNone(sentence.known_safes())

    def test_get_cell_neighbors(self):
        msAi = ms.MinesweeperAI()

        # Top-left's neighbor
        cell = (0,0)
        self.assertEqual(
            msAi.get_cell_neighbors(cell, 0)[0],
            [(0,1), (1,0), (1,1)]
        )

        # Top-Right's neighbor
        cell = (0,7)
        self.assertEqual(
            msAi.get_cell_neighbors(cell, 0)[0],
            [(0,6), (1,6), (1,7)]
        )

        # Bottom-Right's neighbor
        cell = (7,7)
        self.assertEqual(
            msAi.get_cell_neighbors(cell, 0)[0],
            [(6,6), (6,7), (7,6)]
        )

        # Bottom-Left's neighbor
        cell = (7,0)
        self.assertEqual(
            msAi.get_cell_neighbors(cell, 0)[0],
            [(6,0), (6,1), (7,1)]
        )

        # Center's neighbor
        cell = (4,4)
        self.assertEqual(
            msAi.get_cell_neighbors(cell, 0)[0],
            [(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)]
        )

    def test_add_knowledge(self):

        # No neighbor mines
        msAi = ms.MinesweeperAI()
        msAi.add_knowledge((7,0), 0)
        self.assertEqual(msAi.knowledge, [])

        # All neighbor mines
        msAi = ms.MinesweeperAI()
        msAi.add_knowledge((7,7), 3)
        self.assertEqual(msAi.knowledge, [])

        # Unknown
        msAi = ms.MinesweeperAI()
        msAi.add_knowledge((0,0), 1)
        sentence = ms.Sentence([(0,1),(1,0),(1,1)], 1)
        self.assertEqual(msAi.knowledge, [sentence])

        # Example case
        msAi = ms.MinesweeperAI(3, 3)
        msAi.add_knowledge((0,0), 1)
        msAi.add_knowledge((0,1), 1)
        msAi.add_knowledge((0,2), 1)
        msAi.add_knowledge((2,1), 2)
        sentence = ms.Sentence({(2,0),(2,2)}, 1)
        self.assertEqual(msAi.knowledge, [sentence])

    def test_make_safe_move(self):

        # Have safe moves
        msAi = ms.MinesweeperAI(3, 3)
        msAi.add_knowledge((0,0), 1)
        msAi.add_knowledge((0,1), 1)
        msAi.add_knowledge((0,2), 1)
        msAi.add_knowledge((2,1), 2)
        self.assertIsNotNone(msAi.make_safe_move())

        # No safe moves
        msAi = ms.MinesweeperAI()
        msAi.add_knowledge((7,7), 3)
        self.assertIsNone(msAi.make_safe_move())

    def test_make_random_move(self):

        # Any move
        msAi = ms.MinesweeperAI(3, 3)
        msAi.add_knowledge((0,0), 1)
        msAi.add_knowledge((0,1), 1)
        msAi.add_knowledge((0,2), 1)
        msAi.add_knowledge((2,1), 2)
        move = msAi.make_random_move()
        self.assertIsNotNone(move)


if __name__ == "__main__":
    unittest.main()