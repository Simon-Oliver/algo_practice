from tkinter import *

root = Tk()
root.title('Test GUI')
root.geometry('{}x{}'.format(400, 400))

rows = 4
columns = 4

for i in range(rows):
    root.grid_columnconfigure(i, weight=1)
    # The below line is needed to make the frame stick to the bottom when resizing the window
    root.grid_rowconfigure(i, weight=1)

frame_red = Frame(root, bg='red', width=200, height=200)
frame_red.grid(column=0,row=0,sticky='nsew')

frame_red = Frame(root, bg='green', width=200, height=200)
frame_red.grid(column=0,row=1,sticky='nsew')

frame_red = Frame(root, bg='blue', width=200, height=200)
frame_red.grid(column=1,row=0,sticky='nsew')

frame_red = Frame(root, bg='yellow', width=200, height=200)
frame_red.grid(column=1,row=1,sticky='nsew')



root.mainloop()

