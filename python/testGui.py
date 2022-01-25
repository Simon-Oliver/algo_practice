# import tkinter as tk
#
# window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")
# input = tk.Entry()
# def hello():
#     print(input.get())
#     input.delete(0,"end")
# button = tk.Button(text="Hello", command=hello)
# greeting.pack()
# button.pack()
# input.pack()
# window.mainloop()

import tkinter
import customtkinter  # <- import the CustomTkinter module
import sqlite3

con = sqlite3.connect("../chinook.db")
cur = con.cursor()

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("800x680")
root_tk.title("CustomTkinter Test")

def button_function():
    cur.execute(f"SELECT LastName from customers WHERE CustomerId = {entry_1.get()}")
    res = cur.fetchall()
    label_1.set_text(res[0][0])
    entry_1.delete(0,"end")



y_padding = 13

frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

entry_1 = customtkinter.CTkEntry(master=frame_1)
entry_1.pack(pady=y_padding, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=10, command=button_function)
button_1.pack(pady=y_padding, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, text="")
label_1.pack(pady=y_padding, padx=10)

root_tk.mainloop()