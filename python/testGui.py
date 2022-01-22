import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
input = tk.Entry()
def hello():
    print(input.get())
    input.delete(0,"end")
button = tk.Button(text="Hello", command=hello)
greeting.pack()
button.pack()
input.pack()
window.mainloop()
