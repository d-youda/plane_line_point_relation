# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# def plot_cube(ax):
#     # 큐브 그리기
#     vertices = [
#         [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
#         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
#     ]

#     # 정육면체 만들기
#     faces = [
#         [vertices[0], vertices[1], vertices[5], vertices[4]],
#         [vertices[7], vertices[6], vertices[2], vertices[3]],
#         [vertices[0], vertices[4], vertices[7], vertices[3]],
#         [vertices[1], vertices[5], vertices[6], vertices[2]],
#         [vertices[4], vertices[5], vertices[6], vertices[7]],
#         [vertices[0], vertices[1], vertices[2], vertices[3]]
#     ]

#     # Plot the cube by creating a Poly3DCollection of the faces
#     ax.add_collection3d(Poly3DCollection(faces, facecolors='gray', linewidths=1, edgecolors='b', alpha=0.5))

#     # Set axis labels
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')

#     # Set plot limits
#     ax.set_xlim([0, 1])
#     ax.set_ylim([0, 1])
#     ax.set_zlim([0, 1])

# def create_button_frame(root):
#     # 버튼 만들기
#     button_frame = tk.Frame(root, bg='lightgray', width=200, height=root.winfo_screenheight())
#     button_frame.pack_propagate(False)

#     # Create and pack buttons vertically
#     button1 = tk.Button(button_frame, text="Button 1", width=20)
#     button1.pack(side=tk.TOP, pady=5)

#     button2 = tk.Button(button_frame, text="Button 2", width=20)
#     button2.pack(side=tk.TOP, pady=5)

#     button3 = tk.Button(button_frame, text="Button 3", width=20)
#     button3.pack(side=tk.TOP, pady=5)

#     return button_frame
# def on_text_click():
#     print("Text clicked!")  # 이 부분에 원하는 함수의 내용을 추가하십시오.

# def display_gui():
#     root = tk.Tk()
#     root.title("3D Cube and Buttons")

#     # Create a Matplotlib figure and a Tkinter canvas for the cube
#     fig = plt.Figure(figsize=(5, 5), tight_layout=True)
#     ax = fig.add_subplot(111, projection='3d')
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

#     # Plot the cube on the Matplotlib axis
#     plot_cube(ax)
#     def on_label_click(event):
#         on_text_click()
#     # 레이블에 대한 클릭 이벤트 바인딩
#     text_label.bind("<Button-1>", on_label_click)
#     # 텍스트가 표시될 레이블 생성
#     text_label = tk.Label(root, text="Click me!", fg="blue", cursor="hand2")
#     text_label.pack(pady=20)
#     # Create a frame for buttons and pack it on the right side
#     button_frame = create_button_frame(root)
#     button_frame.pack(side=tk.RIGHT, fill=tk.Y)

#     # Show the Tkinter window
#     root.mainloop()

# # # Call the function
# # display_gui()
# import tkinter as tk
# from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# def plot_cube(ax):
#     # Define the eight vertices of the cube
#     vertices = [
#         [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
#         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
#     ]

#     # Define the six faces of the cube using the vertices
#     faces = [
#         [vertices[0], vertices[1], vertices[5], vertices[4]],
#         [vertices[7], vertices[6], vertices[2], vertices[3]],
#         [vertices[0], vertices[4], vertices[7], vertices[3]],
#         [vertices[1], vertices[5], vertices[6], vertices[2]],
#         [vertices[4], vertices[5], vertices[6], vertices[7]],
#         [vertices[0], vertices[1], vertices[2], vertices[3]]
#     ]

#     # Plot the cube by creating a Poly3DCollection of the faces
#     ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

#     # Set axis labels
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')

#     # Set plot limits
#     ax.set_xlim([0, 1])
#     ax.set_ylim([0, 1])
#     ax.set_zlim([0, 1])

# def plot_point(ax, x, y, z):
#     ax.scatter([x], [y], [z], color='red', s=50, marker='o')

# def create_gui():
#     def on_button_click():
#         try:
#             x = float(entry_x.get())
#             y = float(entry_y.get())
#             z = float(entry_z.get())

#             plot_point(ax, x, y, z)
#             canvas.draw()

#         except ValueError:
#             print("Invalid input for x, y, or z")

#     root = tk.Tk()
#     root.title("3D Cube with Points")

#     # Create a Matplotlib figure and a Tkinter canvas for the cube
#     fig = plt.Figure(figsize=(6, 6), tight_layout=True)
#     ax = fig.add_subplot(111, projection='3d')
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

#     # Plot the cube on the Matplotlib axis
#     plot_cube(ax)

#     # Create Entry widgets for x, y, z
#     entry_label_x = tk.Label(root, text="Enter 'x' value:")
#     entry_label_x.pack(pady=5)
#     entry_x = tk.Entry(root)
#     entry_x.pack(pady=5)

#     entry_label_y = tk.Label(root, text="Enter 'y' value:")
#     entry_label_y.pack(pady=5)
#     entry_y = tk.Entry(root)
#     entry_y.pack(pady=5)

#     entry_label_z = tk.Label(root, text="Enter 'z' value:")
#     entry_label_z.pack(pady=5)
#     entry_z = tk.Entry(root)
#     entry_z.pack(pady=5)

#     # Create a Button to add points to the plot
#     button_add_point = tk.Button(root, text="Add Point", command=on_button_click)
#     button_add_point.pack(pady=10)

#     root.mainloop()

# # Call the function to create the GUI
# create_gui()
import tkinter as tk
def show():
    label = tk.Label(root, text=f"pang!")
    label.pack(pady=10)
def show_button():
    # Create a new button
    new_button = tk.Button(root, text="Click Me!",command=show)
    new_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Dynamic Button Example")

# Create a button to trigger the appearance of a new button
trigger_button = tk.Button(root, text="Show Button", command=show_button)
trigger_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
