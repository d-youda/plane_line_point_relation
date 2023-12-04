import tkinter as tk
import numpy as np
from math_method.plane import three_point_plane ,two_plane_angle
from math_method.line import slove_line_and_plane_angle
from math_method.point import two_point_distance,point_and_plane_distance
def create_button_frame(root):
    button_frame = tk.Frame(root, bg='lightgray', width=200, height=root.winfo_screenheight())
    button_frame.pack_propagate(False)

    # Create and pack buttons vertically
    button1 = tk.Button(button_frame, text="Button 1", width=20)
    button1.pack(side=tk.TOP, pady=5)

    button2 = tk.Button(button_frame, text="Button 2", width=20)
    button2.pack(side=tk.TOP, pady=5)

    button3 = tk.Button(button_frame, text="Button 3", width=20)
    button3.pack(side=tk.TOP, pady=5)
def draw_plane(root,ax,plane):
    x, y = np.meshgrid(range(-8, 8), range(-8, 8)) #10x10 array 두 개
    a,b,c = plane
    z = (-a*x - b*x)/c
    ax.plot_surface(x,y,z,color='blue')
    label = tk.Label(root, text=f"{a}x + {b}y + c{z} = 0")
    return label
def draw_point(ax,point):
    ax.scatter(point[0],point[1],point[2],color='red', s=10, marker='o')
    
def add_point(root,ax,point1,point2,point3):
    point1 = np.array([int(point) for point in point1])
    point2 = np.array([int(point) for point in point2])
    point3 = np.array([int(point) for point in point3])

    #점 찍기
    draw_point(ax,point1)
    draw_point(ax,point2)
    draw_point(ax,point3)
    #평면 그리기
    plane = three_point_plane(point1, point2, point3)
    label = draw_plane(root,ax,plane)
    
    return label

def add_plane(root, ax,plane1,plane2):
    plane1 = np.array([int(point) for point in plane1])
    plane2 = np.array([int(point) for point in plane2])

    _ = draw_plane(ax,plane1)
    _ = draw_plane(ax,plane2)
    angle = two_plane_angle(plane1,plane2)
    label = tk.Label(root, text=f"plane1 과 plane2 사이 각도: {angle}")
    return label

def add_plane_and_line(root,ax,plane,line_point1, line_point2):
    plane = np.array([int(point) for point in plane])
    line_point1 = np.array([int(point) for point in line_point1])
    line_point2 = np.array([int(point) for point in line_point2])
    line = [line_point1, line_point2]
    _ = draw_plane(root,ax,plane)

    ax.plot((line_point1[0],line_point1[1],line_point1[2]),(line_point2[0],line_point2[1],line_point2[2]),color='green', label='line')
    ax.legend()
    angle = slove_line_and_plane_angle(plane,line)
    label = tk.Label(root, text=f"평면과 line 사이 각도: {angle}")
    return label

def two_point(root, ax,point1,point2):
    point1 = np.array([int(point) for point in point1])
    point2 = np.array([int(point) for point in point2])
    draw_point(ax,point1)
    draw_point(ax,point2)
    distance = two_point_distance(point1,point2)
    label = tk.Label(root, text=f"두 점 사이 거리 : {distance}")
    return label

def point_and_plane(root,ax,point,plane):
    point = np.array([int(po) for po in point])
    plane = np.array([int(point) for point in plane])
    draw_plane(root,ax,plane)
    draw_point(ax,point)
    distance = point_and_plane_distance(point, plane)
    label = tk.Label(root, text=f"점과 평면 사이의 거리: {distance}")
    return label