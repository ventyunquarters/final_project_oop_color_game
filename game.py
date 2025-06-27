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

    def setup_ui(self):
        # Create the frame where all widgets will be placed
        self.frame = tk.Frame(self.master, bg="#f2f2f2")
        self.frame.pack(expand=True, fill="both")

        # Display game instructions
        self.instructions = tk.Label(self.frame, text="Type the COLOR of the word, not the word text!",
                                     font=('Helvetica', 14), bg="#f2f2f2")
        self.instructions.pack(pady=(20, 10))

        # Label for score updates
        self.scoreLabel = tk.Label(self.frame, text="Press Enter to start",
                                   font=('Helvetica', 12), bg="#f2f2f2")
        self.scoreLabel.pack()

        # Label for time left
        self.timeLabel = tk.Label(self.frame, text="Time left: 30",
                                  font=('Helvetica', 12), fg="red", bg="#f2f2f2")
        self.timeLabel.pack()

        # Label to display the colored word
        self.label = tk.Label(self.frame, font=('Helvetica', 60), bg="#f2f2f2")
        self.label.pack(pady=(20, 10))

        # Entry box where player types their guess
        self.entry = tk.Entry(self.frame, font=('Helvetica', 14), justify='center')
        self.entry.pack()
        self.entry.focus_set()  # Put cursor in the entry box by default