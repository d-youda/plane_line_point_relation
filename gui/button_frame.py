import tkinter as tk
def create_button_frame(root):
    # 버튼 만들기
    button_frame = tk.Frame(root, bg='lightgray', width=200, height=root.winfo_screenheight())
    button_frame.pack_propagate(False)

    # Create and pack buttons vertically
    button1 = tk.Button(button_frame, text="평면", width=20)
    button1.pack(side=tk.TOP, pady=5)

    button2 = tk.Button(button_frame, text="직선", width=20)
    button2.pack(side=tk.TOP, pady=5)

    button3 = tk.Button(button_frame, text="점", width=20)
    button3.pack(side=tk.TOP, pady=5)

    return button_frame