
import tkinter as tk
from tkinter import ttk
import numpy as np
from random import randint
from PIL import ImageTk
from PIL import Image
#from tkinter import PhotoImage
import PIL

class Create_Button(tk.Button):

    def __init__(self, level, row_val, col_val, no_r, no_c, no_b, flag_image, mine_image, current_mine_image, wrong_flag_image, *args, **kwargs):
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
        self.first_bomb = True
        self.state = 0
        self.value = None
        self.flag_image = flag_image
        self.mine_image = mine_image
        self.current_mine_image = current_mine_image
        self.wrong_flag_image = wrong_flag_image
        self.place(width=self.width,
                        height=self.height,
                        x=self.x_val,
                        y=self.y_val)

        self.bind('<Button-3>', self.right_click)

    def not_first_button(self, grid):
        if self.first_button:
            self.first_button = False
            self.grid = grid

    def not_first_bomb(self):
        if self.first_bomb:
            self.first_bomb = False

    def wrong_flag(self):
        self.configure(relief=tk.SUNKEN,
                        state=tk.DISABLED,
                        image=self.wrong_flag_image)

    def left_click(self):
        if self.state == 0:
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

            if self.value == 1:
                self.configure(disabledforeground="blue")
            if self.value == 2:
                self.configure(disabledforeground="green")
            if self.value == 3:
                self.configure(disabledforeground="red")
            if self.value == 4:
                self.configure(disabledforeground="purple")
            if self.value == 5:
                self.configure(disabledforeground="maroon")
            if self.value == 6:
                self.configure(disabledforeground="turquoise")
            if self.value == 7:
                self.configure(disabledforeground="black")
            if self.value == 8:
                self.configure(disabledforeground="gray")

            self.configure(relief=tk.SUNKEN,
                            state=tk.DISABLED,
                            text=str(self.value))

            if self.value == 0:
                self.upper.expanding_zeros(self.r_val, self.c_val)
                self.configure(relief=tk.SUNKEN, state=tk.DISABLED, text="")

            if self.value == 9:
                if self.first_bomb:
                    self.config(relief=tk.SUNKEN,
                                    state=tk.DISABLED,
                                    image=self.current_mine_image)
                else:
                    self.config(relief=tk.SUNKEN,
                                    state=tk.DISABLED,
                                    image=self.mine_image)

                self.upper.game_lost()

            else:
                self.upper.win_cond_counter()



        else:
            pass

    def right_click(self, event):
        if self.value == None:
            if self.state == 0:
                self.state = 1
                self.config(image=self.flag_image)
                self.upper.reduce_counter((self.r_val, self.c_val))
            else:
                self.state = 0
                self.config(image="")
                self.upper.increase_counter((self.r_val, self.c_val))

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

        for i in range(r_val-1, r_val+2):
            for j in range(c_val-1, c_val+2):
                if i == r_val and j == c_val:
                    continue

                if 0 <= i <= no_rows - 1:
                    if 0 <= j <= no_cols - 1:
                        if grid[i, j] != 9:
                            grid[i, j] += 1
                        else:
                            continue
                    else:
                        continue
                else:
                    break

    return grid.astype(int), bomb_locs
