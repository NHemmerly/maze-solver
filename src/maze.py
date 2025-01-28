import time
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
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

    def _create_cell(self):
        position_x = self.x1
        position_y = self.y1
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                self._cells[col].append(Cell(self.win.canvas, position_x, position_x + self.cell_size_x, position_y, position_y + self.cell_size_y))
                position_x += self.cell_size_x
            position_y += self.cell_size_y
        for i in range(len(self._cells)):
            for j in range(len(self._cels[i])):
                self._draw_cell(i, j)
        
    
    def _draw_cell(self, i, j):
        cell_position = (i * self.cell_size_x, j * self.cell_size_y)
        cell_size = (self.cell_size_x * self.cell_size_y)
        maze_position = (self.x1, self.y1)

    def _animate(self):
        self.win.redraw()
        