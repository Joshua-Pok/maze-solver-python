from maze import Maze
from window import Window

def main():

    win = Window(800, 600)
    m = Maze(
        50,
        50,
        10,
        10,
        40,
        40,
        win=win,
        seed=42
    )
    m.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
