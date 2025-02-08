import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )



class TestMaze(unittest.TestCase):

    def test_reset_cells_single_cell(self):
        # Test with 1x1 maze
        maze = Maze(0, 0, 1, 1, 10, 10)
        maze._cells[0][0].visited = True
        maze._reset_cells_visited()
        self.assertFalse(maze._cells[0][0].visited)

    def test_reset_cells_multiple(self):
        # Test 2x2 maze with mixed visited states
        maze = Maze(0, 0, 2, 2, 10, 10)
        
        # Set some cells as visited
        maze._cells[0][0].visited = True
        maze._cells[0][1].visited = True
        maze._cells[1][0].visited = False
        maze._cells[1][1].visited = True

        maze._reset_cells_visited()

        # Verify all cells are reset
        for i in range(2):
            for j in range(2):
                self.assertFalse(maze._cells[i][j].visited)

    def test_reset_cells_multiple_times(self):
        maze = Maze(0, 0, 2, 2, 10, 10)
        
        # Reset multiple times
        for _ in range(3):
            # Set all cells visited
            for i in range(2):
                for j in range(2):
                    maze._cells[i][j].visited = True
            
            maze._reset_cells_visited()

            # Verify reset worked each time
            for i in range(2):
                for j in range(2):
                    self.assertFalse(maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()