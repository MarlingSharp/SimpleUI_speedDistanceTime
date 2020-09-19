import tkinter as tk

# Encapsulate our label as a class
class HelloWorldLabel(tk.Frame):
  def __init__(self, parent):
    super(HelloWorldLabel, self).__init__(parent)

    self.label = tk.Label(self, text="Hello, World!")
    self.label.pack(padx=20, pady=20)