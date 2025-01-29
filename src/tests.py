import unittest

from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_maze_create_more_rows(self):
        num_cols = 12
        num_rows = 24
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_entrance_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[9][9].has_bottom_wall,
            False
        )

    def test_maze_reset(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols, 10, 10)
        self.assertEqual(
            all(map(lambda x: x.visited == False, [cell for cell in[col for col in m1._cells]][0])),
            True
        )

if __name__ == "__main__":
    unittest.main()