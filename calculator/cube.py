import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

value = 500
def plot_cube(ax):
    vertices = [
        [-value, -value, -value], [value, -value, -value], [value, value, -value], [-value, value, -value],
        [-value, -value, value], [value, -value, value], [value, value, value], [-value, value, value]
    ]

    #정육면체 만들기
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[7], vertices[6], vertices[2], vertices[3]],
        [vertices[0], vertices[4], vertices[7], vertices[3]],
        [vertices[1], vertices[5], vertices[6], vertices[2]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[2], vertices[3]]
    ]

    #정육면체 화면에 뿌리기
    ax.add_collection3d(Poly3DCollection(faces, facecolors='lightgray', linewidths=1, edgecolors='black', alpha=0.2))

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot limits
    ax.set_xlim([-value, value])
    ax.set_ylim([-value, value])
    ax.set_zlim([-value, value])

def reset_canvas_and_draw_cube(root,canvas,ax):
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        plot_cube(ax)
        # canvas.draw()