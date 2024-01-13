from tkinter import *

def add_to_input(value):
    current_input = entry.get()
    entry.delete(0, END)
    entry.insert(END, current_input + str(value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

window = Tk()
window.title("Calculator")

entry = Entry(window, width = 16, font = ("Arial", 16))
entry.grid(row = 0, column = 0, columnspan = 4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(window, text = button, padx = 20, pady = 20, font = ("Arial", 16), command = lambda value = button: add_to_input(value) if value != '=' else calculate()).grid(row = row_val, column = col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val +=1

window.mainloop()