from tkinter import *

THEME_COLOR = "#375362"

window = Tk()
window.config(padx=50, pady=50, bg=THEME_COLOR)

canvas = Canvas()
canvas.grid(row=0, column=0)


true_button = Button()

window.mainloop()