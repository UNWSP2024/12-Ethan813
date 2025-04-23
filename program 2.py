import tkinter
import tkinter.messagebox

class Joe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Joe's Automotive")
        self.top_frame = tkinter.Frame(self.window)
        self.bottom_frame = tkinter.Frame(self.window)
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb_var7)
        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')
        self.ok_button = tkinter.Button(self.bottom_frame, text='Calculate Total', command=self.total)
        self.quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.window.destroy)
        self.ok_button.pack(side='left', padx=10)
        self.quit.pack(side='left')
        self.top_frame.pack(padx=20, pady=10)
        self.bottom_frame.pack(pady=10)
        tkinter.mainloop()
    def total(self):
        total = 0
        if self.cb_var1.get() == 1:
            total += 30
        if self.cb_var2.get() == 1:
            total += 20
        if self.cb_var3.get() == 1:
            total += 40
        if self.cb_var4.get() == 1:
            total += 100
        if self.cb_var5.get() == 1:
            total += 35
        if self.cb_var6.get() == 1:
            total += 200
        if self.cb_var7.get() == 1:
            total += 20
        tkinter.messagebox.showinfo('Total Charges', f'Total = ${total:.2f}')
Joe()
#ethan collins 4/23/2025 Who's Joe?