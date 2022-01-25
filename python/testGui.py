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

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x400")
root_tk.title("CustomTkinter Test")



def button_function():
    print("button pressed")

WIDTH = 700
HEIGHT = 500

frame_top = customtkinter.CTkFrame(master=root_tk, corner_radius=10)
frame_top.place(height=200, width=200, relx=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()