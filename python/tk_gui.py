from tkinter import *
import sys

root = Tk()
root.geometry("400x200")
app = Frame(root)
app.grid(row=0, column=0, sticky="")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

title = Label(app,text="My Grid GUI")
title.grid(row=0,columnspan=3)

entries = []

for i in range(1,4):
    label = Label(app,text=f"Field {i}:")
    label.grid(row= i, column=1)
    field = Entry(app)
    field.grid(row=i, column=2)
    entries.append(field)

def get_entry():
    global entries
    text = []
    for e in entries:
        print(e.get())
        e.delete(0,"end")

def close():
    sys.exit()


btn_frame = Frame(app)
btn_frame.grid(row=4,column=2, sticky='e')
button = Button(btn_frame, text="Quit", command=close)
button.pack(side='right')
button = Button(btn_frame, text="Submit", command=get_entry)
button.pack(side='right')

root.mainloop()

