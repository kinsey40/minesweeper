
import tkinter as tk
import numpy as np
from random import randint

class Create_Button(tk.Button):

    def __init__(self, level, row_val, col_val, no_r, no_c, no_b, *args, **kwargs):
        tk.Button.__init__(self, level, command=lambda: self.left_click())
        self.upper = level
        self.width = 20
        self.height = 20
        self.c_val = col_val
        self.r_val = row_val
        self.no_r = no_r
        self.no_c = no_c
        self.no_b = no_b
        self.x_val = self.c_val * self.width
        self.y_val = self.r_val * self.height
        self.first_button = True
        self.state = 0
        self.value = None

        self.place(width=self.width,
                        height=self.height,
                        x=self.x_val,
                        y=self.y_val)

        self.bind('<Button-3>', self.right_click)

    def not_first_button(self, grid):
        if self.first_button:
            self.first_button = False
            self.grid = grid

    def left_click(self):
        if self.first_button:
            self.grid, self.bomb_locs = create_array(self.no_r,
                                            self.no_c,
                                            self.no_b,
                                            self.r_val,
                                            self.c_val)

            self.upper.first_button_press(self.r_val,
                                            self.c_val,
                                            self.grid,
                                            self.bomb_locs)

        self.value = self.grid[self.r_val, self.c_val]

        if self.value == 9:
            self.configure(relief=tk.SUNKEN,
                            state=tk.DISABLED,
                            text=str(self.value))
            self.upper.game_lost()

        else:
            self.upper.win_cond_counter()
            self.configure(relief=tk.SUNKEN,
                            state=tk.DISABLED,
                            text=str(self.value))

        if self.value == 0:
            self.upper.expanding_zeros(self.r_val, self.c_val)

    def right_click(self, event):
        if self.value == None:
            if self.state == 0:
                self.state = 1
                self.upper.reduce_counter()
            else:
                self.state = 0
                self.upper.increase_counter()

    def disable_button(self):
        self.configure(state=tk.DISABLED)

def create_array(no_rows, no_cols, no_bombs, row_val, col_val):

    count = 0
    bomb_locs = []
    grid = np.zeros((no_rows, no_cols))

    while count < no_bombs:
        random_row = randint(0, no_rows-1)
        random_col = randint(0, no_cols-1)

        if (random_row, random_col) == (row_val, col_val) or \
            (random_row, random_col) in bomb_locs:
            continue
        else:
            count += 1
            bomb_locs.append((random_row, random_col))

    for loc in bomb_locs:
        r_val = loc[0]
        c_val = loc[1]

        grid[r_val, c_val] = 9

        if r_val == 0 and c_val == 0:
            grid[r_val, c_val+1] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val+1, c_val+1] += 1

        elif r_val == 0 and c_val == no_cols - 1:
            grid[r_val, c_val-1] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val+1, c_val-1] += 1

        elif c_val == 0 and r_val == no_rows - 1:
            grid[r_val-1, c_val] += 1
            grid[r_val-1, c_val+1] += 1
            grid[r_val, c_val+1] += 1

        elif c_val == no_cols - 1 and r_val == no_rows - 1:
            grid[r_val-1, c_val-1] += 1
            grid[r_val-1, c_val] += 1
            grid[r_val, c_val-1] += 1

        elif r_val == 0:
            grid[r_val, c_val-1] += 1
            grid[r_val, c_val+1] += 1
            grid[r_val+1, c_val-1] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val+1, c_val+1] += 1

        elif r_val == no_rows - 1:
            grid[r_val-1, c_val-1] += 1
            grid[r_val-1, c_val] += 1
            grid[r_val-1, c_val+1] += 1
            grid[r_val, c_val-1] += 1
            grid[r_val, c_val+1] += 1

        elif c_val == 0:
            grid[r_val-1, c_val] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val-1, c_val+1] += 1
            grid[r_val, c_val+1] += 1
            grid[r_val+1, c_val+1] += 1

        elif c_val == no_cols - 1:
            grid[r_val-1, c_val] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val-1, c_val-1] += 1
            grid[r_val, c_val-1] += 1
            grid[r_val+1, c_val-1] += 1

        else:
            grid[r_val-1, c_val-1] += 1
            grid[r_val-1, c_val] += 1
            grid[r_val-1, c_val+1] += 1
            grid[r_val, c_val-1] += 1
            grid[r_val, c_val+1] += 1
            grid[r_val+1, c_val-1] += 1
            grid[r_val+1, c_val] += 1
            grid[r_val+1, c_val+1] += 1

        np.place(grid, grid > 9, 9)

    return grid.astype(int), bomb_locs
