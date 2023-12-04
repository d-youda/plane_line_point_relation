import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import plot_cube
from action_function import three_point_make_plane,two_plane_angles,plane_and_line_angle

root = tk.Tk()
root.title("3D 큐브에 그리는 화면")

#화면 왼쪽에 큐브 그릴 캔버스 삽입
fig = plt.Figure(figsize=(5, 5), tight_layout=True)
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
plot_cube(ax)

def three_point_event():
    three_point_make_plane(root,ax,canvas)
def two_plane_event():
    two_plane_angles(root,ax,canvas)
def plane_and_line_event():
    plane_and_line_angle(root,ax,canvas)
def show_plane_button():
    # Create a new button
    three_point_button = tk.Button(root, text="세 점을 잇는 평면 그리기", command=three_point_event)
    three_point_button.pack(pady=15)
    two_plane_angle = tk.Button(root, text="두 평면 사이의 각도 구하기",command=two_plane_event)
    two_plane_angle.pack(pady=15)
def show_line_button():
    plane_line_angle = tk.Button(root, text="평면과 라인 간 각도 구하기",command=plane_and_line_angle)
    plane_line_angle.pack(side=tk.TOP,pady=10)

button1 = tk.Button(root, text="평면",command=show_plane_button,width=20)
button1.pack(side=tk.TOP, pady=20)
button2 = tk.Button(root, text="라인",command=show_line_button,width=20)
button2.pack(side=tk.TOP, pady=20)
button3 = tk.Button(root, text='점', width=20)
root.mainloop()

