import tkinter as tk
import tkinter.font as tkFont

"""
Simple demo of encapsulating a UI element as a class
"""
class Title(tk.Frame):
  def __init__(self, parent):
    super(Title, self).__init__(parent)

    # Create a font we can use throughout
    fontStyle = tkFont.Font(size=24)

    self.label = tk.Label(self, text="Physics Calculator", font=fontStyle)
    self.label.pack(padx=20, pady=20)