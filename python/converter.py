import tkinter
import sys


class CelsiusGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Create the widgets for the top frame
        self.celsius_label = tkinter.Label(self.top_frame, text='Enter the Celsius temperature: ')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)
        # Pack the top frame widgets
        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        self.far_label = tkinter.Label(self.mid_frame, text='Farenheit temperature: ')
        self.far_label.pack(side='left')
        self.farenheit = tkinter.StringVar()
        self.farenheit_label = tkinter.Label(self.mid_frame, textvariable=self.farenheit)
        self.farenheit_label.pack(side="left")



        self.button = tkinter.Button(self.bottom_frame, text="Convert", command=self.c_to_f)
        self.button.pack(side="left")
        self.button_quit = tkinter.Button(self.bottom_frame, text="Quit", command=sys.exit)
        self.button_quit.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def c_to_f(self):
        c = float(self.celsius_entry.get())
        f = (9 / 5) * c + 32
        format = "{:.2f}".format(f)
        self.farenheit.set(format)




# Create an instance of CelsiusGUI
celsius = CelsiusGUI()
