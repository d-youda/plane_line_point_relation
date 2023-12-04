import tkinter as tk
def entry_label(root, text):
    entry_label = tk.Label(root, text=text)
    entry_label.pack(side=tk.TOP, pady=5)
    entry = tk.Entry(root)
    entry.pack(side=tk.TOP, pady=5)
    return entry