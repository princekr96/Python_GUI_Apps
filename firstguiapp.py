from tkinter import *

window = Tk()

# to rename the title of the window
window.title("First App")

# pack is used to show the objet in the window
label = Label(window, text="First GUI app", font=("Arial Bold", 50)).grid()

bt = Button(window, text="Enter")
bt.grid(column=0, row=2)

window.mainloop()