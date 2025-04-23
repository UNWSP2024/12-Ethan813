import tkinter as tk
from tkinter import messagebox

def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return

        result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Divide Numbers")


tk.Label(root, text="Enter miles driven:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter gallons of gas:").pack()
entry2 = tk.Entry(root)
entry2.pack()


divide_button = tk.Button(root, text="Divide", command=divide_numbers)
divide_button.pack()


result_label = tk.Label(root, text="Miles Per Gallon: ")
result_label.pack()

root.mainloop()
#MPG calculator 4/22/2025 Ethan collins