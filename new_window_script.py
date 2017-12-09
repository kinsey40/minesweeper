# Creates a new window

import tkinter as tk
from tkinter import ttk
from buttons_script import Create_Button
import numpy as np
import time

class MainWindow(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.launch_button = tk.Button(self, text="Launch",
                                command=self.create_window)
        self.launch_button.place(width=80, height=40, x=60, y=250)
        self.modes = [
            ("Beginner", 1),
            ("Intermediate", 2),
            ("Expert", 3),
            ("Custom", 4)
        ]
        self.value = 0
        self.create_welcome_text()
        self.create_radio_buttons()
        self.window = False
        self.no_bombs = 0
        self.no_cols = 0
        self.no_rows = 0
        self.error_indicator = 0
        self.custom = False
        self.e_text = tk.Label(self, text="", justify=tk.CENTER)

    def create_welcome_text(self):
        self.welcome_text = tk.Label(self, text="Welcome to Minsweeper", justify=tk.CENTER)
        self.welcome_text.pack(anchor=tk.CENTER)
        self.welcome_text.config(font=("Courier", 12))
        self.welcome_text.place(x=15, y=10)

    def create_radio_buttons(self):
        self.v = tk.IntVar()
        self.v.set(0)

        for i, (text, value) in enumerate(self.modes):
            b = tk.Radiobutton(self,
                            text=text,
                            variable=self.v,
                            value=value,
                            command=self.set_values)
            b.pack(anchor=tk.W)
            b.place(x=50, y=50 + (i * 30))

    def set_values(self):
        self.e_text['text'] = " " * len(self.e_text['text'])
        self.value = self.v.get()

        if self.value == 1:
            if self.custom:
                self.custom = False
                self.bomb_entry.destroy()
                self.rows_entry.destroy()
                self.cols_entry.destroy()
                self.bomb_label.destroy()
                self.rows_label.destroy()
                self.cols_label.destroy()

            self.no_bombs = 10
            self.no_cols = 9
            self.no_rows = 9

        if self.value == 2:
            if self.custom:
                self.custom = False
                self.bomb_entry.destroy()
                self.rows_entry.destroy()
                self.cols_entry.destroy()
                self.bomb_label.destroy()
                self.rows_label.destroy()
                self.cols_label.destroy()

            self.no_bombs = 15
            self.no_cols = 14
            self.no_rows = 14

        if self.value == 3:
            if self.custom:
                self.custom = False
                self.bomb_entry.destroy()
                self.rows_entry.destroy()
                self.cols_entry.destroy()
                self.bomb_label.destroy()
                self.rows_label.destroy()
                self.cols_label.destroy()

            self.no_bombs = 30
            self.no_cols = 19
            self.no_rows = 19

        if self.value == 4:
            self.custom = True
            self.custom_inputs()

    def custom_inputs(self):
        self.bomb_label = tk.Label(self, text="No. of bombs:")
        self.rows_label = tk.Label(self, text="No. of rows:")
        self.cols_label = tk.Label(self, text="No. of cols:")
        self.bomb_entry = tk.Entry(self)
        self.rows_entry = tk.Entry(self)
        self.cols_entry = tk.Entry(self)

        self.bomb_label.place(x=15, y=165)
        self.rows_label.place(x=15, y=185)
        self.cols_label.place(x=15, y=205)
        self.bomb_entry.place(x=125, y=165, width=45)
        self.rows_entry.place(x=125, y=185, width=45)
        self.cols_entry.place(x=125, y=205, width=45)

    def set_window_var(self):
        if not self.window:
            self.window = True
        else:
            self.window = False

    def error_text(self):
        self.e_text.config(font=("Courier", 8))

        if self.error_indicator == 1:
            self.e_text.place(x=30, y=230)
            self.e_text.config(text="Please select an option")

        if self.error_indicator == 2:
            self.e_text.place(x=30, y=230)
            self.e_text.config(text="Entries must be integer")

        if self.error_indicator == 3:
            self.e_text.place(x=5, y=230)
            self.e_text.config(text="No. of rows must be 19 or less")

        if self.error_indicator == 4:
            self.e_text.place(x=5, y=230)
            self.e_text.config(text="No. of cols must be 19 or less")

        if self.error_indicator == 5:
            self.e_text.place(x=5, y=230)
            self.e_text.config(text="No. of rows must be 8 or larger")

        if self.error_indicator == 6:
            self.e_text.place(x=5, y=230)
            self.e_text.config(text="No. of cols must be 8 or larger")

        if self.error_indicator == 7:
            self.e_text.place(x=15, y=230)
            self.e_text.config(text="Too many bombs for grid size")

        if self.error_indicator == 8:
            self.e_text.place(x=30, y=230)
            self.e_text.config(text="Missing an input value")


    def create_window(self):
        if self.value == 0:
            self.error_indicator = 1
            self.error_text()
            return 1

        if self.value == 4:
            if not self.bomb_entry.get().strip() or not \
                        self.rows_entry.get().strip() or not \
                        self.cols_entry.get().strip():
                self.error_indicator = 8
                self.error_text()
                return

            if not self.bomb_entry.get().isdigit() or not \
                        self.rows_entry.get().isdigit() or not \
                        self.cols_entry.get().isdigit():
                self.error_indictor = 2
                self.error_text()
                return

            if int(self.rows_entry.get()) > 19:
                self.error_indicator = 3
                self.error_text()
                return

            if int(self.cols_entry.get()) > 19:
                self.error_indicator = 4
                self.error_text()
                return

            if int(self.rows_entry.get()) < 7:
                self.error_indicator = 5
                self.error_text()
                return

            if int(self.cols_entry.get()) < 7:
                self.error_indicator = 6
                self.error_text()
                return

            if int(self.bomb_entry.get()) >= \
                    int(self.rows_entry.get()) * int(self.cols_entry.get()):
                self.error_indicator = 7
                self.error_text()
                return

            self.no_bombs = int(self.bomb_entry.get())
            self.no_rows = int(self.rows_entry.get())
            self.no_cols = int(self.cols_entry.get())

        if not self.window:
            self.e_text['text'] = " " * len(self.e_text['text'])
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
        self.geometry('{}x{}'.format(no_c*20+400, no_r*20+20))
        self.win_counter = 0
        self.top = top
        self.no_bombs = no_bombs
        self.no_c = no_c
        self.no_r = no_r
        self.end_text = tk.Label(self)
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
                        x=self.no_c*20+300,
                        y=10)

        change_settings_button = tk.Button(self, text="Change Settings", \
                                command=self.on_closing)
        change_settings_button.place(width=120,
                        height=20,
                        x=self.no_c*20+150,
                        y=10)

        reset_button = tk.Button(self, text="Reset", command=self.reset_grid)
        reset_button.place(width=50,
                        height=20,
                        x=self.no_c*20+50,
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

        index = (r * self.no_c) + c
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

            self.end_text.pack()
            self.end_text.config(font=("Courier", 44), text="You Win!")
            self.end_text.place(x=(self.no_c * 20 + 80),
                            y=self.no_r * 20 - 60)

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

        self.end_text.pack()
        self.end_text.config(font=("Courier", 44), text="You Lose!")
        self.end_text.place(x=(self.no_c * 20 + 80),
                        y=self.no_r * 20 - 60)

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
        self.counter_label.place(x=self.no_c * 20+100, y=50)

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
    root.geometry('{}x{}'.format(200, 300))
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":

    create_main_window()
