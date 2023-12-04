import tkinter as tk

def enter_the_equation(root,value):
    label = tk.Label(root,text=f"{value}: ")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    entry = tk.Entry(root)
    entry.grid(row=0, column=1, padx=10, pady=10)
    return entry