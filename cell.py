from tkinter import Canvas
from line import Line
from point import Point


class Cell():
    def __init__(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1



    def draw(self, x1: int, y1: int, x2: int, y2: int, canvas: Canvas):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2


        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)



        left_wall = Line(top_left, bottom_left )
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)
        


        if self.has_left_wall:
            left_wall.draw("black", canvas)


        if self.has_right_wall:
            right_wall.draw("black", canvas)

        if self.has_top_wall:
            top_wall.draw("black", canvas)

        if self.has_bottom_wall:
            bottom_wall.draw("black", canvas)


    def draw_move(self, canvas: Canvas, to_cell: "Cell", undo=False,):
        if not undo:
            color = "red"
        else:
            color = "gray"


        curr_mid_x = (self.__x1 + self.__x2) // 2 
        curr_mid_y = (self.__y1 + self.__y2) // 2


        curr_mid = Point(curr_mid_x, curr_mid_y)


        to_mid_x = (to_cell.__x1 + to_cell.__x2) // 2
        to_mid_y = (to_cell.__y1 + to_cell.__y2) // 2


        to_mid = Point(to_mid_x, to_mid_y)
        

        connector = Line(curr_mid, to_mid)
        connector.draw(color, canvas)




