from window import Window
from maze import Maze

def main():
    print("Hello Maze Solver")
    win = Window(800, 600)
    maze = Maze(20, 10, 6, 8, 95, 95, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()