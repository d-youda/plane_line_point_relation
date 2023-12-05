import tkinter as tk
import numpy as np
from math_method.plane import three_point_plane ,two_plane_angle,two_point_one_plane,two_plane_one_point
from math_method.line import slove_line_and_plane_angle,solve_two_line_angle
from math_method.point import two_point_distance,point_and_plane_distance
def list_to_numpy(list):
    lists = np.array([int(point) for point in list])
    return lists
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
    '''평면 그리는 함수'''
    if np.shape(plane) == (4,):
        x, y = np.meshgrid(range(-5, 5), range(-5, 5)) #10x10 array 두 개
        a,b,c,d = plane
        z = (d-a*x - b*y)/c
        ax.plot_surface(x,y,z,color='blue')
        label = tk.Label(root, text=f"{a}x + {b}y + {c}z = {d}")
    elif np.shape(plane)==(3,):
        x, y = np.meshgrid(range(-5, 5), range(-5, 5)) #10x10 array 두 개
        a,b,c = plane
        z = (-a*x - b*y)/c
        ax.plot_surface(x,y,z,color='blue')
        label = tk.Label(root, text=f"{a}x + {b}y + {c}z = 0")        
    return label
def draw_point(ax,point):
    '''점 그리는 함수'''
    ax.scatter(point[0],point[1],point[2],color='red', s=10, marker='o')

def draw_line(ax,point,dir_vector):
    '''직선 그리는 함수'''
    def parametric_line(ax,t, point, dir_vector):
        x,y,z = point
        a,b,c = dir_vector
        x_value = x + a * t
        y_value = y + b * t
        z_value = z + c * t
        ax.scatter([x], [y], [z], color='red', marker='o', label='Starting Point')
        return x_value, y_value, z_value
    t_values = np.linspace(0,5,100)
    x_values,y_values,z_values = parametric_line(ax,t_values,point,dir_vector)
    ax.plot(x_values,y_values,z_values)
    
def add_point(root,ax,point1,point2,point3):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    point3 = list_to_numpy(point3)
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

    _ = draw_plane(root,ax,plane1)
    _ = draw_plane(root,ax,plane2)
    angle = two_plane_angle(plane1,plane2)
    label = tk.Label(root, text=f"plane1 과 plane2 사이 각도: {angle}")
    return label

def add_plane_and_line(root,ax,plane,line_point1, line_dir_vec):
    plane = list_to_numpy(plane)
    line_point1 = list_to_numpy(line_point1)
    line_dir_vec = list_to_numpy(line_dir_vec)
    draw_plane(root,ax,plane)
    draw_line(ax,line_point1,line_dir_vec)
    angle = slove_line_and_plane_angle(plane,line_point1,line_dir_vec)
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

def points_and_mid_points_plane(root,ax,orbitale_1,orbitale_2,porion_1,porion_2):
    orbitale_1 = np.array([int(point) for point in orbitale_1])
    orbitale_2 = np.array([int(point) for point in orbitale_2])
    porion_1 = np.array([int(point) for point in porion_1])
    porion_2 = np.array([int(point) for point in porion_2])

    mid_porion = np.array([int((porion_2[0]+porion_1[0])/2),(porion_2[1]+porion_1[1])/2,(porion_2[2]+porion_1[2])/2])
    draw_point(ax,orbitale_1)
    draw_point(ax,orbitale_2)
    draw_point(ax,porion_1)
    draw_point(ax,porion_2)
    draw_point(ax,mid_porion)

    #평면 그리기
    plane = three_point_plane(orbitale_1, orbitale_2, mid_porion)
    label = draw_plane(root,ax,plane)
    
    return label

def two_point_one_plane_solve(root,ax,point1,point2,plane):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    plane = list_to_numpy(plane)

    draw_point(ax,point1)
    draw_point(ax,point2)
    draw_plane(root,ax,plane)

    solve_plane = two_point_one_plane(point1,point2,plane)
    label = draw_plane(root,ax,solve_plane)
    return label

def solve_one_point_two_plane(root, ax,point, plane1, plane2):
    point = list_to_numpy(point)
    plane1 = list_to_numpy(plane1)
    plane2 = list_to_numpy(plane2)

    draw_point(ax,point)
    draw_plane(root,ax,plane1)
    draw_plane(root,ax,plane2)
    solve_plane = two_plane_one_point(point,plane1,plane2)
    label = draw_plane(root,ax,solve_plane)
    return label

def solve_two_lines_angle(root, ax,line1_point, line1_dir_vec, line2_point, line2_dir_vec):
    '''두 직선의 각도 구하는 공식'''
    line1_point = list_to_numpy(line1_point)
    line1_dir_vec = list_to_numpy(line1_dir_vec)
    line2_point = list_to_numpy(line2_point)
    line2_dir_vec = list_to_numpy(line2_dir_vec)
    draw_line(ax,line1_point,line1_dir_vec)
    draw_line(ax,line2_point,line2_dir_vec)
    degree = solve_two_line_angle(line1_dir_vec,line2_dir_vec)
    
    label = tk.Label(root, text=f"두 직선이 이루는 각도: {degree}")
    return label

