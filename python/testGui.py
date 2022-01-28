
# import tkinter
# import customtkinter  # <- import the CustomTkinter module
# import sqlite3
#
# con = sqlite3.connect("../chinook.db")
# cur = con.cursor()
#
# root_tk = tkinter.Tk()  # create the Tk window like you normally do
# root_tk.geometry("800x680")
# root_tk.title("CustomTkinter Test")
#
# def button_function():
#     cur.execute(f"SELECT LastName from customers WHERE CustomerId = {entry_1.get()}")
#     res = cur.fetchall()
#     label_1.set_text(res[0][0])
#     entry_1.delete(0,"end")
#
#
#
# y_padding = 13
#
# frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)
#
# entry_1 = customtkinter.CTkEntry(master=frame_1)
# entry_1.pack(pady=y_padding, padx=10)
#
# button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=10, command=button_function)
# button_1.pack(pady=y_padding, padx=10)
#
# label_1 = customtkinter.CTkLabel(master=frame_1, text="")
# label_1.pack(pady=y_padding, padx=10)
#
# root_tk.mainloop()

from tkinter import *

root = Tk()
root.title('Test GUI')
root.geometry('{}x{}'.format(460, 350))

isHidden = False
frame_L = ""

def create_L_frame():
    global frame_L
    frame_L = Frame(root, bg='#6b705c', width=120, height=350, pady=3)
    frame_L.grid(column=0, row=0, sticky="nsew")
    return frame_L

def hide():
    global isHidden
    global frame_L
    if not isHidden:
        frame_L.destroy()
        isHidden = True
    else:
        create_L_frame()
        isHidden = False

frame_R = Frame(root, bg='#a5a58d', width=360, height=350, pady=3)
create_L_frame()

root.grid_columnconfigure(1,weight=4)
# The below line is needed to make the frame stick to the bottom when resizing the window
root.grid_rowconfigure(0,weight=1)


frame_R.grid(column=1,row=0,sticky="nsew")
frame_R.grid_columnconfigure(1, weight=1)
frame_R.grid_rowconfigure(1, weight=1)

canvas = Canvas(frame_R, width=289, height=289)
canvas.grid(column=1, row=1)
img = PhotoImage(file="./image/helloworld.png")
canvas.create_image(0,0, anchor=NW, image=img)

btn = Button(frame_R,text='Hide Left Menu', command=hide, highlightbackground='#a5a58d')
btn.grid(column=1, row=0,pady=100,padx=100)

root.mainloop()