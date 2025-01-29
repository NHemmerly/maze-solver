from point import Line, Point

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        point_1 = Point(x1, y1)
        point_2 = Point(x2, y2)
        point_3 = Point(x2, y1)
        point_4 = Point(x1, y2)
        left_line = Line(point_1, point_4)
        top_line = Line(point_1, point_3)
        right_line = Line(point_2, point_3)
        bottom_line = Line(point_2, point_4)
        blank = "#d9d9d9"
        if self.has_left_wall:
            left_line.draw(self._win.canvas, "black")
        else: left_line.draw(self._win.canvas, blank)
        if self.has_top_wall:
            top_line.draw(self._win.canvas, "black")
        else: top_line.draw(self._win.canvas, blank)
        if self.has_right_wall:
            right_line.draw(self._win.canvas, "black")
        else: right_line.draw(self._win.canvas, blank)
        if self.has_bottom_wall:
            bottom_line.draw(self._win.canvas, "black")
        else: bottom_line.draw(self._win.canvas, blank)
        

    def draw_move(self, to_cell, undo=False):
        line = Line(Point((self._x2 + self._x1) / 2, (self._y1 + self._y2) / 2), Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y1 + to_cell._y2) / 2))
        if undo:
            line.draw(self._win.canvas, "gray")
        else:
            line.draw(self._win.canvas, "red")



        