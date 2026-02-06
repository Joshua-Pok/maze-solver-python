from tkinter import Canvas, Tk
from point import Point


class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


    def draw(self, color: str, canvas: Canvas):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)

