import tkinter
import tkinter.messagebox

class Calls:
    def __init__(self):
        self.window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02 per min',variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12 per min', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-Peak (midnight through 5:59 P.M.) 	$0.05 per min', variable=self.radio_var, value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.time = tkinter.Entry(self.top_frame)
        self.time.pack()
        self.ok_button =tkinter.Button(self.bottom_frame, text='OK',command=self.calculate)
        self.ok_button.pack(side='left')
        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.window.destroy)
        self.quit.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        length = float(self.time.get())
        if self.radio_var.get() == 1:
            rate = 0.02
        elif self.radio_var.get() == 2:
            rate = 0.12
        else:
            rate = 0.05
        cost = length * rate
        tkinter.messagebox.showinfo('cost', f'Total cost is : ${cost:.2f}')
Calls()
#ethan collins 4/23/2025 calls