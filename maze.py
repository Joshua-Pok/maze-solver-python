from cell import Cell
import time

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
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__cells = []
        self.__win = win


    def __create_cells(self):

        self.__cells = [Cell() for _ in range(self.cell_size_x) for _ in range(self.cell_size_y)] # creates number of rowsa


    def __draw_cell(self, i , j):
        # i have top left coords
        # i have size of each cell
        # i need to find the top left and bottom right coords of the cell [i][j]

        target = self.__cells[i][j]

        target_top_left_x = self.__x1 + i * self.cell_size_x
        target_top_left_y = self.__y1


        target_bottom_right_x = target_top_left_x + self.cell_size_x
        target_bottom_right_y = target_top_left_y + self.cell_size_y


        cell = Cell()
        cell.draw(target_top_left_x,target_top_left_y,target_bottom_right_x,target_bottom_right_y)


        self.__animate()


    def __animate(self):
        self.__win.redraw()
        time.sleep(0.5)






