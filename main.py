"""
With thanks to
https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app

"""

# Import the library
import tkinter as tk

# Import our custom components
from Title import Title
from SpeedForm import SpeedForm

# Create our application
root = tk.Tk()

# Create our custom components
main = Title(root)
form = SpeedForm(root)

# Add our components to the root
main.pack(fill="both", expand=True)
form.pack()

""" 
User Interfaces (and games) usually setup their rules and then enter into an 'infinite loop'. 
During each run through the loop the state of the program
is advanced and any user events are handled
"""
root.mainloop()