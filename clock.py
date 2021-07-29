# import turtle library
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("DIGITAL CLOCK IN PYTHON")

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000, time)

label = Label(root, font=("Digital-7", 45), background = "blue", foreground = "yellow", )
label.pack(anchor='center')
#root.wm_attributes("-transparentcolor","blue")

time()

root.mainloop()