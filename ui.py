import tkinter as tk
from game import GameLogic
from sound import SoundManager

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("COLOR GAME")
        self.master.geometry("450x300")
        self.master.resizable(False, False)

        self.logic = GameLogic()
        self.sound = SoundManager()

        self.setup_ui()
        self.master.bind('<Return>', self.start_game)

    def setup_ui(self):
        self.frame = tk.Frame(self.master, bg="#f2f2f2")
        self.frame.pack(expand=True, fill="both")

        self.instructions = tk.Label(self.frame, text="Type the COLOR of the word, not the word text!",
                                     font=('Helvetica', 14), bg="#f2f2f2")
        self.instructions.pack(pady=(20, 10))

        self.scoreLabel = tk.Label(self.frame, text="Press Enter to start",
                                   font=('Helvetica', 12), bg="#f2f2f2")
        self.scoreLabel.pack()

        self.timeLabel = tk.Label(self.frame, text="Time left: 30",
                                  font=('Helvetica', 12), fg="red", bg="#f2f2f2")
        self.timeLabel.pack()

        self.label = tk.Label(self.frame, font=('Helvetica', 60), bg="#f2f2f2")
        self.label.pack(pady=(20, 10))

        self.entry = tk.Entry(self.frame, font=('Helvetica', 14), justify='center')
        self.entry.pack()
        self.entry.focus_set()

    def start_game(self, event=None):
        if self.logic.timeleft == 30:
            self.countdown()
        self.next_colour()

    def next_colour(self):
        if self.logic.timeleft > 0:
            self.entry.focus_set()
            if self.logic.check_answer(self.entry.get()):
                self.sound.play_correct()

            self.entry.delete(0, tk.END)
            text, color = self.logic.next_colours()
            self.label.config(fg=color, text=text)
            self.scoreLabel.config(text="Score: " + str(self.logic.score))

    def countdown(self):
        if self.logic.timeleft > 0:
            self.logic.timeleft -= 1
            self.timeLabel.config(text="Time left: " + str(self.logic.timeleft))
            self.master.after(1000, self.countdown)
        else:
            self.end_game()

    def end_game(self):
        self.label.config(text="You Win!", fg="green")
        self.scoreLabel.config(text=f"Final Score: {self.logic.score}", font=('Helvetica', 14, 'bold'))
        self.timeLabel.config(text="Time's up!", fg="red")
        self.entry.config(state='disabled')
        self.sound.play_gameover()