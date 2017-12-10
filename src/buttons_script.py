"""
Author: Nicholas Kinsey (kinsey40)

Date: 10/12/2017

Description:
This file contains the Create_Button class, which is used to define how the
buttons in the grid behave when clicked.

Also contained within this file is the create array function, which decides
where the mines should be placed and calculates the relevant numbers for the
other buttons in the grid.
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from random import randint


class Create_Button(tk.Button):
    """Initializes the buttons in the grid.

    Args:
        level (obj: tkinter window): The 'Game Window'.
        row_val (int): The row value for that particular button in the grid.
        col_val (int): The col value for that particular button in the grid.
        no_r (int): The number of rows in the grid.
        no_c (int): The number of cols in the grid.
        no_b (int): The number of bombs in the grid.
        flag_image (obj: tkinter.PhotoImage): The flag image to be used.
        mine_image (obj: tkinter.PhotoImage): The mine image to be used.
        current_mine_image (obj: tkinter.PhotoImage): The current mine image.
        wrong_flag_image (obj: tkinter.PhotoImage): The 'incorrect' flag image.

    Attributes:
        upper (obj: tkinter window): The 'Game Window'.
        width: (int): The width of each button in the grid
        height (int): The height of each button in the grid
        c_val (int): The col value for that particular button in the grid.
        r_val (int): The row value for that particular button in the grid.
        no_r (int): The number of rows in the grid.
        no_c (int): The number of cols in the grid.
        no_b (int): The number of bombs in the grid.
        x_val (int): Where to place the button in the window (horizontal).
        y_val (int): Where to place the button in the window (vertical).
        first_button (bool): True if button is first button to be clicked.
        first_bomb (bool): True if this is the first bomb found.
        state (int): Zero if no flag displayed, one otherwise.
        value (int): Value that the button should display.
        flag_image (obj: tkinter.PhotoImage): The flag image to be used.
        mine_image (obj: tkinter.PhotoImage): The mine image to be used.
        current_mine_image (obj: tkinter.PhotoImage): The current mine image.
        wrong_flag_image (obj: tkinter.PhotoImage): The 'incorrect' flag image.

    """
    def __init__(
                    self, level, row_val, col_val, no_r, no_c, no_b,
                    flag_image, mine_image, current_mine_image,
                    wrong_flag_image, *args, **kwargs
                ):
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
        self.place(
                    width=self.width,
                    height=self.height,
                    x=self.x_val,
                    y=self.y_val)
        self.bind('<Button-3>', self.right_click)

    def not_first_button(self, grid):
        """ Identifies if this button is the first button or not.

        Args:
            grid (obj: np.array): The grid of numbers defining button values

        """
        if self.first_button:
            self.first_button = False
            self.grid = grid

    def not_first_bomb(self):
        """ Identifies if this is the first bomb clicked or not."""
        if self.first_bomb:
            self.first_bomb = False

    def wrong_flag(self):
        """ Displays the 'wrong flag image' on the relevant button."""
        self.configure(relief=tk.SUNKEN,
                       state=tk.DISABLED,
                       image=self.wrong_flag_image)

    def left_click(self):
        """ This is the callback for the left click of a button in the grid.

        Identifies whether the button is the first button to be clicked, if so,
        it ensures the 'click is free', by calling the relevant functions in
        the NewWindow class.

        It also calls the create_array function, which outputs a numpy array
        corresponding to the numbers for the buttons in the grid.

        The button text colours are set here, as well as the expanding zeros
        feature called from inside the NewWindow class.

        Finally, the function registers the value of the button clicked, so as
        to call whether it is a mine or not and also to increase the win
        counter from within the NewWindow class.

        """
        if self.state == 0:
            if self.first_button:
                self.grid, self.bomb_locs = create_array(
                                                            self.no_r,
                                                            self.no_c,
                                                            self.no_b,
                                                            self.r_val,
                                                            self.c_val)

                self.upper.first_button_press(
                                                self.r_val,
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

            self.configure(
                            relief=tk.SUNKEN,
                            state=tk.DISABLED,
                            text=str(self.value))

            if self.value == 0:
                self.upper.expanding_zeros(self.r_val, self.c_val)
                self.configure(relief=tk.SUNKEN, state=tk.DISABLED, text="")

            if self.value == 9:
                if self.first_bomb:
                    self.config(
                                    relief=tk.SUNKEN,
                                    state=tk.DISABLED,
                                    image=self.current_mine_image)
                else:
                    self.config(
                                    relief=tk.SUNKEN,
                                    state=tk.DISABLED,
                                    image=self.mine_image)

                self.upper.game_lost()

            else:
                self.upper.win_cond_counter()

        else:
            pass

    def right_click(self, event):
        """ Defines button behaviour when button is 'right-clicked'.

        Args:
            event: ('<Button-3>'): The tkinter event that has been performed.

        If image on button is already a flag, removes flag. The relevant
        functions in NewWindow are called to ensure the 'mines counter'
        is reduced or increased appropriately.

        """
        if self.value is None:
            if self.state == 0:
                self.state = 1
                self.config(image=self.flag_image)
                self.upper.reduce_counter((self.r_val, self.c_val))
            else:
                self.state = 0
                self.config(image="")
                self.upper.increase_counter((self.r_val, self.c_val))

    def disable_button(self):
        """ Disable the button."""
        self.configure(state=tk.DISABLED)


def create_array(no_rows, no_cols, no_bombs, row_val, col_val):
    """ Creates the grid of numbers from which the buttons obtain their values.

    Randomly chooses the bomb locations, by choosing random integers between 0
    and the relevant row or column number. Assigns the number '9' to bomb
    locations as each button is surrounded by 8 other buttons (maximum).

    Args:
        no_rows (int): No. of rows in the grid
        no_cols (int): No. of columns in the grid
        no_bombs (int): No. of bombs in the grid
        row_val (int): The row value for the first clicked button
        col_val (int): The column value for the first clicked button

    Returns:
        grid (obj: np.array(int)): A grid of values for the button values
        bomb_locs (list): List of tuples for bomb locations (row, column).

    """

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
