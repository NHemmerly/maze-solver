from window import Window
from point import Line, Point

def main():
    print("Hello Maze Solver")
    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(800, 600))
    line2 = Line(Point(0, 600), Point(800, 0))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()