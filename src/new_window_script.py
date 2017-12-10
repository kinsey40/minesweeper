"""
Author: Nicholas Kinsey (kinsey40)

Date: 10/12/2017

Description:
This file contains two classes. The MainWindow class sets up the
'Game Settings' window, from which the game may be launched.

The second class sets up the 'Game Window', calling the buttons class to
populate the grid and insert various other buttons to perform the required
functionality.
"""

import tkinter as tk
from tkinter import ttk
from .buttons_script import Create_Button


class MainWindow(tk.Frame):
    """ Sets up the Game Settings window

    The window is populated with 'beginner', 'intermediate', 'expert' and
    'custom' buttons. Many checks are performed on the custom setting,
    preventing the user from inputting values which eitther create poor
    formatting in the game window, or result in stack overflow issues.

    """

    def __init__(self, *args, **kwargs):
        """ Initialize the window with various parameters

        The main widgets on the 'Game Settings' window are initialized here,
        with various parameters also being defined.

        Attributes:
            launch_button (obj: tkinter.Button): The button that launches Game.
            modes (obj: list): The difficulty modes, with set numbers.
            value (int): The value corresponding to the difficulty.
            window (bool): Whether a 'Game Window' is open.
            no_bombs (int): No. of bombs to be used in game.
            no_cols (int): No. of columns to be used in game.
            no_rows (int): No. of rows to be used in game.
            error_indicator (int): Which error the user needs to respond to.
            custom (bool): Whether the 'custom' setting is selected.
            e_text (tkinter.Label): The error text to be displayed.

        """
        tk.Frame.__init__(self, *args, **kwargs)
        self.launch_button = tk.Button(
                                        self,
                                        text="Launch",
                                        command=self.create_window)
        self.modes = [
            ("Beginner", 1),
            ("Intermediate", 2),
            ("Expert", 3),
            ("Custom", 4)
        ]
        self.value = 0
        self.window = False
        self.no_bombs = 0
        self.no_cols = 0
        self.no_rows = 0
        self.error_indicator = 0
        self.custom = False
        self.e_text = tk.Label(self, text="", justify=tk.CENTER)
        self.launch_button.place(width=80, height=40, x=60, y=250)
        self.create_welcome_text()
        self.create_radio_buttons()

    def create_welcome_text(self):
        """ Create the welcome text at the top of the window."""
        self.welcome_text = tk.Label(
                                        self,
                                        text="Welcome to Minsweeper",
                                        justify=tk.CENTER)
        self.welcome_text.pack(anchor=tk.CENTER)
        self.welcome_text.config(font=("Courier", 12))
        self.welcome_text.place(x=15, y=10)

    def create_radio_buttons(self):
        """ Create the radio buttons, defining game difficulty setting.

        The buttons all link to the same variable, with different values.
        These values enable the program to understand the difficulty setting
        chosen by the user.

        """
        self.v = tk.IntVar()
        self.v.set(0)

        for i, (text, value) in enumerate(self.modes):
            b = tk.Radiobutton(
                                self,
                                text=text,
                                variable=self.v,
                                value=value,
                                command=self.set_values)
            b.pack(anchor=tk.W)
            b.place(x=50, y=50 + (i * 30))

    def set_values(self):
        """ Reads the value of the radio button variable, sets game values.

        Further, if the 'custom' setting was previously selected, the widgets
        corresponding to the entry boxes and labels are destroyed.

        If the error text exists from entering previous values, this is also
        destroyed.

        """
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
        """ Create the entry and label widgets needed for a custom game."""
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
        """ Helps to ensure only one game window is open at any one time."""
        if not self.window:
            self.window = True
        else:
            self.window = False

    def error_text(self):
        """ Writes an error message to the window."""
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
        """ Create the game window.

        Perform the various checks, particularly if this is a custom game.
        Calls the error_text function to output the relevant message to the
        screen.

        """
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
                self.no_bombs,
                self.no_cols,
                self.no_rows
            )

        else:
            pass

    def quit_program(self):
        """ Closes the program."""
        self.quit()


class NewWindow(tk.Toplevel, MainWindow):
    """ Creates the 'Game Window.'

    This class creates the 'Game Window'. Firstly, it sets up many of the
    various widgets, which allow the user to 'reset', 'quit' and
    'change settings'.

    Further, it also sets up and displays a mines left counter and a win/loss
    text display.

    Finally, the buttons are created by calling the Create_Button class.

    Args:
        top (obj: tkinter.Tk): The top level window ('Game Settings').
        no_bombs (int): The number of bombs in the game.
        no_c (int): The number of columns to use in the grid.
        no_r (int): The number of rows to use in the grid.

    Attributes:
        win_counter (int): Counts the number of correctly clicked buttons.
        top (obj: tkinter.Tk): The top level window ('Game Settings').
        no_bombs (int): The number of bombs in the game.
        no_c (int): The number of columns to use in the grid.
        no_r (int): The number of rows to use in the grid.
        end_text (obj: tkinter.Label): The text displayed upon games' end.
        flag_image (obj: tkinter.PhotoImage): The flag image to be used.
        mine_image (obj: tkinter.PhotoImage): The mine image to be used.
        current_mine_image (obj: tkinter.PhotoImage): The current mine image.
        wrong_flag_image (obj: tkinter.PhotoImage): The 'incorrect' flag image.
        resized_flag (obj: tkinter.PhotoImage): Resized image
        resized_mine (obj: tkinter.PhotoImage): Resized image
        resized_current_mine (obj: tkinter.PhotoImage): Resized image
        resized_incorrect_flag (obj: tkinter.PhotoImage): Resized image
        all_buttons (list): List which will hold the buttons.
        flag_locs (list): List of tuples corresponding to flag locations.
        bombs_counter (int): A counter regarding the number of mines to find.

    """
    def __init__(self, top, no_bombs, no_c, no_r, *args, **kwargs):
        tk.Toplevel.__init__(self)
        self.win_counter = 0
        self.top = top
        self.no_bombs = no_bombs
        self.no_c = no_c
        self.no_r = no_r
        self.end_text = tk.Label(self)
        self.flag_image = tk.PhotoImage(file="images/flag.gif")
        self.mine_image = tk.PhotoImage(file="images/mine.gif")
        self.current_mine_image = tk.PhotoImage(file="images/current_mine.gif")
        self.incorrect_flag_image = tk.PhotoImage(file="images/wrong_flag.gif")
        self.resized_flag = self.flag_image.subsample(5, 5)
        self.resized_mine = self.mine_image.subsample(15, 15)
        self.resized_current_mine = self.current_mine_image.subsample(15, 15)
        self.resized_incorrect_flag = \
            self.incorrect_flag_image.subsample(15, 15)
        self.all_buttons = []
        self.flag_locs = []
        self.bombs_counter = self.no_bombs
        self.geometry('{}x{}'.format(self.no_c*20+400, self.no_r*20+20))
        self.wm_title("Minesweeper")
        self.create_button_grid()
        self.create_option_buttons()
        self.create_mines_counter()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_option_buttons(self):
        """ Creates the various option buttons in the window."""
        quit_button = tk.Button(self, text="Quit", command=self.quit_program)
        quit_button.place(
                            width=50,
                            height=20,
                            x=self.no_c*20+300,
                            y=10)

        change_settings_button = tk.Button(
                                            self,
                                            text="Change Settings",
                                            command=self.on_closing)
        change_settings_button.place(
                                        width=120,
                                        height=20,
                                        x=self.no_c*20+150,
                                        y=10)

        reset_button = tk.Button(self, text="Reset", command=self.reset_grid)
        reset_button.place(
                            width=50,
                            height=20,
                            x=self.no_c*20+50,
                            y=10)

    def create_button_grid(self):
        """ Creates the grid of buttons, by calling the Create_Button class."""
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
        """ Ensures that the first click the user makes is 'free'.

        Args:
            r (int): Clicked buttons' row value.
            c (int): Clicked buttons' column value.
            grid (obj: np.array): Array equating to the values of the buttons.
            bomb_locs (list): List of tuples representing bomb locations.

        Attributes:
            two_d_list (list of lists): List holding the buttons.

        """
        self.bomb_locs = bomb_locs
        self.two_d_list = [
                            self.all_buttons[i:i+self.no_c] for i in
                            range(0, len(self.all_buttons), self.no_c)]

        index = (r * self.no_c) + c
        [b.not_first_button(grid) for i, b
            in enumerate(self.all_buttons) if i != index]

        self.all_buttons = None

    def expanding_zeros(self, r, c):
        """ Defines the 'expanding zeros' feature.

        This is performed by invoking the callback of the buttons that surround
        a square of value 0.

        This method is called from inside the Create_Button class.

        Args:
            r (int): The row value for the clicked button.
            c (int): The column value for the clicked button.

        """
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
        """ Defines the win condition, called within Create_Button class."""
        self.win_counter += 1

        if self.win_counter >= (self.no_r * self.no_c) - self.no_bombs:
            for loc in self.bomb_locs:
                if loc in self.flag_locs:
                    continue
                else:
                    r_val = loc[0]
                    c_val = loc[1]
                    b = self.two_d_list[r_val][c_val]
                    b.right_click('<Button-3>')

            [[b.disable_button() for b in line] for line in self.two_d_list]

            self.end_text.pack()
            self.end_text.config(font=("Courier", 44), text="You Win!")
            self.end_text.place(
                                x=self.no_c * 20 + 80,
                                y=self.no_r * 20 - 60)

    def game_lost(self):
        """ Called when a mine is clicked from inside Create_Button class.

        It invokes all the bomb callbacks, so the user can see where the bombs
        are hidden, it also uses a different image for the specific mine the
        user clicked.

        The program also identifies incorrect 'flagging' of squares by the user
        and displays the relevant image in this case.

        """
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
        self.end_text.place(
                            x=self.no_c * 20 + 80,
                            y=self.no_r * 20 - 60)

    def reduce_counter(self, loc):
        """ Reduces the 'no. of mines to find' counter by one.

        Args:
            loc (tuple): Tuple (row_val, col_val) for the flag location.

        """
        self.flag_locs.append(loc)
        self.bombs_counter -= 1
        self.counter_label['text'] = \
            "Number of mines to find: {}".format(self.bombs_counter)

    def increase_counter(self, loc):
        """ Increases the 'no. of mines to find' counter by one.

        Args:
            loc (tuple): Tuple (row_val, col_val) for the flag location.

        """
        self.flag_locs.remove(loc)
        self.bombs_counter += 1
        self.counter_label['text'] = \
            "Number of mines to find: {}".format(self.bombs_counter)

    def create_mines_counter(self):
        """ Creates the 'mines left' counter widget."""
        self.counter_label = tk.Label(
                                self,
                                text=(
                                    "Number of mines to find: {}"
                                    .format(self.bombs_counter)))
        self.counter_label.pack()
        self.counter_label.place(x=self.no_c * 20+100, y=50)

    def reset_grid(self):
        """ Resets game by destroying and recalling widgets in the window."""
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
        """ Closes the 'Game window', but keeps 'Game Settings' window open."""
        self.destroy()
        MainWindow.set_window_var(self.top)

    def quit_program(self):
        """ Exits the entire program."""
        MainWindow.quit_program(self.top)


def create_main_window():
    """ Used to create the Game Settings window.

    Program initialized by calling this function.

    """
    root = tk.Tk()
    root.wm_title("Game Settings")
    main = MainWindow(root)
    root.geometry('{}x{}'.format(200, 300))
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
