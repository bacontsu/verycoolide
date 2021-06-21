import tkinter as tk

class StatusBar:
    def ShowStatus(self):
        statusbar = tk.Label(text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)

        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
