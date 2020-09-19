import tkinter as tk
import tkinter.font as tkFont

from physics import calculate_speed

class SpeedForm(tk.Frame):
  def __init__(self, parent):
    super(SpeedForm, self).__init__(parent)

    # Create a font we can use throughout
    fontStyle = tkFont.Font(size=20)

    self.lbl_distance = tk.Label(self, text='Distance (m)', font=fontStyle)
    self.txt_distance = tk.Entry(self, font=fontStyle)
    
    self.lbl_time = tk.Label(self, text='Time (s)', font=fontStyle)
    self.txt_time = tk.Entry(self, font=fontStyle)

    self.cmd_calculate = tk.Button(
      self,
      text='Calculate',
      width=25, 
      font=fontStyle,
      command=self.on_click
    )

    self.lbl_speed = tk.Label(self, text='Speed (m/s)', font=fontStyle)
    self.lbl_speed_output = tk.Label(self, font=fontStyle)

    # Put components onto screen
    self.lbl_distance.pack()
    self.txt_distance.pack()
    self.lbl_time.pack()
    self.txt_time.pack()
    self.cmd_calculate.pack(padx=20, pady=20)
    self.lbl_speed.pack()
    self.lbl_speed_output.pack()

  def on_click(self):
    # Read out the string values
    distance_m_str = self.txt_distance.get()
    time_s_str = self.txt_time.get()

    # Do the conversion to floats
    distance_m = float(distance_m_str)
    time_s = float(time_s_str)

    speed = calculate_speed(distance_m, time_s)
    self.lbl_speed_output['text'] = f"{round(speed,2)} m/s"
    