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

    def start_game(self, event):
        # Start the countdown timer on first press of Enter
        if self.timeleft == 30:
            self.countdown()

        # Show the first color word
        self.next_colour()

    def next_colour(self):
        # Only continue if game is still running
        if self.timeleft > 0:
            self.entry.focus_set()  # Keep entry box focused for user input

            # Check if user's input matches the color (not the text)
            if self.entry.get().lower() == self.colours[1].lower():
                self.score += 1        # Increase score
                self.sound.play_correct()  # Play correct-answer sound

            self.entry.delete(0, tk.END)  # Clear input box

            random.shuffle(self.colours)  # Randomize color order

            # Display the next color word and set its font color
            self.label.config(fg=self.colours[1], text=self.colours[0])

            # Update score label
            self.scoreLabel.config(text="Score: " + str(self.score))

    def countdown(self):
        # If time still remains
        if self.timeleft > 0:
            self.timeleft -= 1  # Decrease time by 1 second

            # Update time label
            self.timeLabel.config(text="Time left: " + str(self.timeleft))

            # Call this function again after 1 second
            self.master.after(1000, self.countdown)
        else:
            self.end_game()  # When time runs out, end the game
