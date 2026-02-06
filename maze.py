from cell import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.__win = win
        self.seed = seed


        if self.seed is not None:
            random.seed(self.seed)


        self.__create_cells()


    # __ only used for when we never want outside access
    def __create_cells(self):
        self._cells = [
            [Cell() for _ in range(self.num_cols)]
            for _ in range(self.num_rows)
        ]

    def _draw_cell(self, i , j):
        # i have top left coords
        # i have size of each cell
        # i need to find the top left and bottom right coords of the cell [i][j]

        target = self._cells[i][j]

        x1 = self.__x1 + j * self.cell_size_x

        y1 = self.__y1 + i * self.cell_size_y


        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        if self.__win is None:
            return

        target.draw(x1, y1, x2, y2, self.__win.canvas)


        self.__animate()


    def __animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.1)


    def draw(self):
        self.__create_cells()


        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._draw_cell(r, c)


        self._break_walls(0,0)

        self._break_entrance_and_exit()



    def _break_entrance_and_exit(self):
        # Remove top wall of the top left cell by setting has_top_wall = false
        topLeftCell = self._cells[0][0]
        topLeftCell.has_top_wall = False
        self._draw_cell(0, 0)

        # remove bottom wall of bottom right cell 

        bottomRightCell = self._cells[self.num_rows - 1][self.num_cols - 1]
        bottomRightCell.has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

        # call self._draw_cell() after each removal to update the display


    def _break_walls(self, i, j):
        # depth first traversal breaking walls as we go
        # we need to keep breaking until we find the exit
        # maze carving steps"
        # look at all unvisited neighbours
        # if none -> backtrack
        # if there are some choose a random neighbour
        # break wall between current and neighbur
        # mark neigbour as visited and continue

        stack = []
        root = (i, j)
        stack.append(root)
        while stack:
            r, c = stack.pop()
            self._cells[r][c].visited = True

            neighbours = []

            for dr, dc in [(1,0), (-1,0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if nr < self.num_rows and nr >= 0 and nc < self.num_cols and nc >= 0 and not self._cells[nr][nc].visited:
                    neighbours.append((nr, nc, dr, dc)) # we need the dr and dc to know relative position of neighbour to current


            if not neighbours:
                continue


            stack.append((r,c))
            nr, nc, dr, dc = random.choice(neighbours) # randomly choose a neighbour
            self._cells[nr][nc].visited = True


            if dr == 1:
                self._cells[r][c].has_bottom_wall = False
                self._cells[nr][nc].has_top_wall = False
                self._draw_cell(r, c)
                self._draw_cell(nr, nc)

            elif dr == -1:
                self._cells[r][c].has_top_wall = False
                self._cells[nr][nc].has_bottom_wall = False
                self._draw_cell(r, c)
                self._draw_cell(nr, nc)
            elif dc == 1:
                self._cells[r][c].has_right_wall = False
                self._cells[nr][nc].has_left_wall = False
                self._draw_cell(r, c)
                self._draw_cell(nr, nc)

            elif dc == -1:
                self._cells[r][c].has_left_wall = False
                self._cells[nr][nc].has_right_wall = False
                self._draw_cell(r, c)
                self._draw_cell(nr, nc)


            stack.append((nr, nc))


    def __reset_cells_visited(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._cells[r][c].visited = False











