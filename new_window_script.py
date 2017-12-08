# Creates a new window

import tkinter as tk
from tkinter import ttk
from buttons_script import Create_Button
import numpy as np
import time

class MainWindow(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Launch",
                                command=self.create_window)
        self.button.place(width=80, height=40, x=100, y=100)
        self.window = False
        self.no_bombs = 10
        self.no_cols = 9
        self.no_rows = 9

    def set_window_var(self):
        if not self.window:
            self.window = True
        else:
            self.window = False

    def create_window(self):
        if not self.window:
            self.set_window_var()
            t = NewWindow(
                self,
                self.window,
                self.no_bombs,
                self.no_cols,
                self.no_rows
            )

        else:
            pass

    def quit_program(self):
        self.quit()

class NewWindow(tk.Toplevel, MainWindow):

    def __init__(self, top, w, no_bombs, no_c, no_r, *args, **kwargs):
        tk.Toplevel.__init__(self)
        self.geometry('{}x{}'.format(no_r*20+400, no_c*20+20))
        self.win_counter = 0
        self.top = top
        self.no_bombs = no_bombs
        self.no_c = no_c
        self.no_r = no_r
        self.flag_image = tk.PhotoImage(file="flag.gif")
        self.mine_image = tk.PhotoImage(file="mine.gif")
        self.current_mine_image = tk.PhotoImage(file="current_mine.gif")
        self.incorrect_flag_image = tk.PhotoImage(file="wrong_flag.gif")
        self.resized_flag = self.flag_image.subsample(5,5)
        self.resized_mine = self.mine_image.subsample(15,15)
        self.resized_current_mine = self.current_mine_image.subsample(15,15)
        self.resized_incorrect_flag = self.incorrect_flag_image.subsample(15,15)
        self.all_buttons = []
        self.flag_locs = []
        self.wm_title("Minesweeper")
        self.bombs_counter = self.no_bombs
        self.create_button_grid()
        self.create_option_buttons()
        self.create_mines_counter()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_option_buttons(self):
        quit_button = tk.Button(self, text="Quit", command=self.quit_program)
        quit_button.place(width=50,
                        height=20,
                        x=self.no_r*20+300,
                        y=10)

        change_settings_button = tk.Button(self, text="Change Settings", \
                                command=self.on_closing)
        change_settings_button.place(width=120,
                        height=20,
                        x=self.no_r*20+150,
                        y=10)

        reset_button = tk.Button(self, text="Reset", command=self.reset_grid)
        reset_button.place(width=50,
                        height=20,
                        x=self.no_r*20+50,
                        y=10)

    def create_button_grid(self):
        for row in range(self.no_r):
            for col in range(self.no_c):
                but = Create_Button(self, row,
                                    col, self.no_r,
                                    self.no_c, self.no_bombs,
                                    self.resized_flag, self.resized_mine,
                                    self.resized_current_mine,
                                    self.resized_incorrect_flag)
                self.all_buttons.append(but)

    def first_button_press(self, r, c, grid, bomb_locs):
        self.bomb_locs = bomb_locs
        self.two_d_list = [self.all_buttons[i:i+self.no_c] for i in \
                            range(0, len(self.all_buttons), self.no_c)]

        index = (r * self.no_r) + c
        [b.not_first_button(grid) for i, b in enumerate(self.all_buttons) \
            if i != index]

        self.all_buttons = None

    def expanding_zeros(self, r, c):
        buttons_to_invoke = []
        o_index = (r * self.no_r) + c

        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i == r and j == c:
                    continue

                if 0 <= i <= self.no_r - 1:
                    if 0 <= j <= self.no_c - 1:
                        buttons_to_invoke.append((i, j))
                    else:
                        continue
                else:
                    break

        for count, (row, col) in enumerate(buttons_to_invoke):
            b = self.two_d_list[row][col]
            b.invoke()

    def win_cond_counter(self):
        self.win_counter += 1

        if self.win_counter >= (self.no_r * self.no_c) - self.no_bombs:
            [[b.disable_button() for b in line] for line in self.two_d_list]

            self.end_text = tk.Label(self, text="You Win!")
            self.end_text.pack()
            self.end_text.config(font=("Courier", 44))
            self.end_text.place(x=(self.no_r * 20 + 60),
                            y=self.no_c * 20 - 80)

    def game_lost(self):
        for loc in self.bomb_locs:
            r_val = loc[0]
            c_val = loc[1]
            b = self.two_d_list[r_val][c_val]
            b.not_first_bomb()
            b.invoke()

        for loc in self.flag_locs:
            if loc in self.bomb_locs:
                continue
            else:
                r_val = loc[0]
                c_val = loc[1]
                b = self.two_d_list[r_val][c_val]
                b.wrong_flag()

        [[b.disable_button() for b in line] for line in self.two_d_list]

        self.end_text = tk.Label(self, text="You Lose!")
        self.end_text.pack()
        self.end_text.config(font=("Courier", 44))
        self.end_text.place(x=(self.no_r * 20 + 60),
                        y=self.no_c * 20 - 80)

    def reduce_counter(self, loc):
        self.flag_locs.append(loc)
        self.bombs_counter -= 1
        self.counter_label['text'] = \
                "Number of mines to find: {}".format(self.bombs_counter)

    def increase_counter(self, loc):
        self.flag_locs.remove(loc)
        self.bombs_counter += 1
        self.counter_label['text'] = \
                "Number of mines to find: {}".format(self.bombs_counter)

    def create_mines_counter(self):
        self.counter_label = tk.Label(self, \
                text="Number of mines to find: {}".format(self.bombs_counter))
        self.counter_label.pack()
        self.counter_label.place(x=self.no_r * 20+100, y=50)

    def reset_grid(self):
        [[b.destroy() for b in line] for line in self.two_d_list]
        self.counter_label.destroy()
        self.end_text['text'] = " " * len(self.end_text['text'])

        self.win_counter = 0
        self.flag_locs = []
        self.bombs_counter = self.no_bombs
        self.all_buttons = []

        self.create_button_grid()
        self.create_mines_counter()

    def on_closing(self):
        self.destroy()
        MainWindow.set_window_var(self.top)

    def quit_program(self):
        MainWindow.quit_program(self.top)

def create_main_window():
    root = tk.Tk()
    root.wm_title("Game Settings")
    main = MainWindow(root)
    root.geometry('{}x{}'.format(600, 600))
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":

    create_main_window()
