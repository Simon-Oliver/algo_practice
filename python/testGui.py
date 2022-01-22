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

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()