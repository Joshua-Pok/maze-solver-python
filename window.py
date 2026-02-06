from tkinter import Tk, BOTH, Canvas

from cell import Cell
from line import Line

class Window():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False
        self.cells = [...]
        

    def redraw(self): # clear the canvas and draw everything again
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
            self.root.update_idletasks()
            self.root.update()


    def close(self):
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def draw_line(self, line: Line, color: str):
        line.draw(color, self.canvas)


