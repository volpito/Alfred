import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

class Calculator:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Calculator')

        frame = tk.Frame(self.win, bg="skyblue", padx=10)
        frame.pack()

        self.entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
        self.entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
        buttons = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
        ('*', 5, 2), ('/', 6, 0)
    ]
        
        for txt, r, c in buttons:
            tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: self.click(t)).grid(row=r, column=c, pady=2)

        tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=self.clear).grid(row=6, column=1, columnspan=2, pady=2)
        tk.Button(frame, text="=", padx=15, pady=5, width=9, command=self.equal).grid(row=7, column=0, columnspan=3, pady=2)

        self.win.mainloop()
        

    def click(self, num):
        self.entry.insert(tk.END, num)


    def equal(self):
        try:
            res = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, res)
        except:
            tk.messagebox.showinfo("Error", "Syntax Error")


    def clear(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    Calculator()