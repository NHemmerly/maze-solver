import time
import random
from cell import Cell

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._seed = seed
        self._cells = []

        if not seed == None:
            self._seed = random.seed(seed)

        self._create_cell()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cell(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                self._cells[col].append(Cell(self.win))
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
        
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1,len(self._cells[-1]) - 1)

    def _possible_paths(self, i, j):
        possible = []
        right = i + 1
        left = i - 1
        up = j - 1
        down = j + 1
        if right < len(self._cells):
            if not self._cells[right][j].visited: possible.append((right, j))
        if left >= 0:
            if not self._cells[left][j].visited: possible.append((left, j))
        if up >= 0:
            if not self._cells[i][up].visited: possible.append((i, up))
        if down < len(self._cells[i]):
            if not self._cells[i][down].visited: possible.append((i, down))
        return possible

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            to_visit.extend(self._possible_paths(i, j))
            if len(to_visit) == 0: 
                self._draw_cell(i, j)
                return
            direction = to_visit[random.randrange(len(to_visit))]
            breakage = (direction[0] - i, direction[1] - j)
            if breakage[0] > 0:
                self._cells[i][j].has_right_wall = False
            elif breakage[0] < 0:
                self._cells[i][j].has_left_wall = False
            elif breakage[1] > 0:
                self._cells[i][j].has_bottom_wall = False
            elif breakage[1] < 0:
                self._cells[i][j].has_top_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)