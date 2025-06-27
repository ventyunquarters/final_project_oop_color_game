# main.py
import tkinter as tk
from game import ColorGame

def main():
    root = tk.Tk()
    app = ColorGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()