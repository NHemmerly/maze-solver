from window import Window
from cell import Cell

def main():
    print("Hello Maze Solver")
    win = Window(800, 600)
    cell1 = Cell(win.canvas, 1, 100, 1, 100)
    cell1.has_right_wall = False
    cell2 = Cell(win.canvas, 100, 200, 1, 100)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3 = Cell(win.canvas, 100, 200, 100, 200)
    cell3.has_top_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    win.wait_for_close()


if __name__ == "__main__":
    main()