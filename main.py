# Import the library
import tkinter as tk

from HelloWorldLabel import HelloWorldLabel

# Create our application
root = tk.Tk()

main = HelloWorldLabel(root)
main.pack(fill="both", expand=True)

""" 
User Interfaces (and games) usually setup their rules and then enter into an 'infinite loop'. 
During each run through the loop the state of the program
is advanced and any user events are handled
"""
root.mainloop()