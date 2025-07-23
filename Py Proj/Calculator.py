import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

class Calculator:

    def __init__(self):
        self.entry = ""
        

    def Equal(self):
        print('Type "EXIT" to exit calculus program')        
        while "exit" not in self.entry.casefold():
            self.entry = input("-> ").strip()
            try:
                res = str(eval(self.entry))
                print(res)
            except:
                if 'exit' in self.entry.casefold():
                    break
                else:
                    tk.messagebox.showinfo("Error", "Syntax Error")


    def clear(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    Calculator().Equal()