import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import plot_cube
from action_function import three_point_make_plane,two_plane_angles,plane_and_line_angle,two_points_distance,point_and_plane_distance,point_and_mid_point_plane

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

def two_point_event():
    two_points_distance(root,ax,canvas)
def plane_and_point_event():
    point_and_plane_distance(root,ax,canvas)
def point_and_mid_point_event():
    point_and_mid_point_plane(root,ax,canvas)
def show_plane_button():
    #평면과 관련된 연산들
    three_point_button = tk.Button(root, text="세 점을 잇는 평면 그리기", command=three_point_event)
    three_point_button.pack(pady=15)
    two_plane_angle = tk.Button(root, text="두 평면 사이의 각도 구하기",command=two_plane_event)
    two_plane_angle.pack(pady=15)

def show_line_button():
    #라인과 관련된 연산들
    plane_line_angle = tk.Button(root, text="평면과 라인 간 각도 구하기",command=plane_and_line_event)
    plane_line_angle.pack(side=tk.TOP,pady=10)

    two_line_angle = tk.Button(root, text="라인과 라인 간 각도 구하기")
    two_line_angle.pack(side=tk.TOP,pady=10)

def show_point_button():
    two_point_distance = tk.Button(root, text="두 점 사이 거리 구하기",command=two_point_event)
    two_point_distance.pack(side=tk.TOP,pady=10)
    point_and_plane = tk.Button(root, text="점과 평면 사이 거리 구하기", command=plane_and_point_event)
    point_and_plane.pack(side=tk.TOP,pady=10)
    point_mid_point = tk.Button(root, text="좌/우 orbitale 두 점과 좌/우 portion의 중간 점을 지나는 평면",command=point_and_mid_point_event)
    point_mid_point.pack(side=tk.TOP, pady=10)

button1 = tk.Button(root, text="평면",command=show_plane_button,width=20)
button1.pack(side=tk.TOP, pady=20)
button2 = tk.Button(root, text="라인",command=show_line_button,width=20)
button2.pack(side=tk.TOP, pady=20)
button3 = tk.Button(root, text='점', command=show_point_button,width=20)
button3.pack(side=tk.TOP, pady=20)

root.mainloop()