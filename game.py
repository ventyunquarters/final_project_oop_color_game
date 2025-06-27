#color game
import tkinter as tk
import random
from sound import SoundManager


class ColorGame:
    def __init__(self, master):
        # Initialize the main window (Tkinter root)
        self.master = master
        self.master.title("COLOR GAME")
        self.master.geometry("450x300") # Set window size
        self.master.resizable(False, False) # Prevent resizing

        # Initialize the SoundManager to handle game sounds
        self.sound = SoundManager()

        # List of color names to use in the game
        self.colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                        'Yellow', 'Orange', 'White', 'Purple', 'Brown']

        self.score = 0           # Initialize score
        self.timeleft = 30       # Countdown timer starts at 30 seconds

        self.setup_ui()          # Call method to build the GUI layout

        # Bind the Enter key to start the game
        self.master.bind('<Return>', self.start_game)
