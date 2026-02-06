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
        self.canvas.delete("all")
        padding = 50

        x1 = padding
        y1 = padding

        x2 = self.width - padding
        y2 = self.height - padding
        # --- test cells ---
        rows = 2
        cols = 2

        cell_width = (x2 - x1) // cols
        cell_height = (y2 - y1) // rows

        for r in range(rows):
            for c in range(cols):
                cx1 = x1 + c * cell_width
                cy1 = y1 + r * cell_height
                cx2 = cx1 + cell_width
                cy2 = cy1 + cell_height

                cell = Cell()
                cell.draw(cx1, cy1, cx2, cy2, self.canvas)

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


