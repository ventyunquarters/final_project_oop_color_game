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