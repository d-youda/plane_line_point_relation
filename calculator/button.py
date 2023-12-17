import tkinter as tk
import numpy as np
from matplotlib.lines import Line2D
from math_method.plane import three_point_plane ,two_plane_angle,two_point_one_plane,two_plane_one_point,one_parallel_plane_and_point
from math_method.line import slove_line_and_plane_angle,solve_two_line_angle
from math_method.point import two_point_distance,point_and_plane_distance,three_point_angle_solve,middle_two_point
def list_to_numpy(list):
    lists = np.array([float(point) for point in list])
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
    
def draw_plane(root,ax,plane,label=None,color='blue',vertical=False):
    '''평면 그리는 함수'''
    if vertical:
        x, y = np.meshgrid(range(-100, 100), range(-100, 100)) #10x10 array 두 개
    else:
        x, y = np.meshgrid(range(-200, 200), range(-200, 200)) #10x10 array 두 개
    a,b,c,d = plane
    z = (d-a*x - b*y)/c
    ax.plot_surface(x,y,z,label=f'{label}',color=color,alpha=0.5)
    legend_elements = [Line2D([0], [0], color=color, lw=2, label=f'{label}')]
    legend = ax.legend(handles=legend_elements, loc='upper right')
    ax.add_artist(legend)
    label = tk.Label(root, text="%s : %.2fx + %.2fy + %.2fz = %.2f"%(label,a,b,c,d))        
    return label

def draw_point(ax,point,color='red'):
    '''점 그리는 함수'''
    ax.scatter(point[0],point[1],point[2],color=color, s=10, marker='o')

def draw_line(ax,point1,point2):
    '''직선 그리는 함수'''
    ax.plot((point1[0],point2[0]),(point1[1],point2[1]),(point1[2],point2[2]),color='green')
    
def three_points_plane(root,ax,point1,point2,point3,labels):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    point3 = list_to_numpy(point3)
    #점 찍기
    draw_point(ax,point1)
    draw_point(ax,point2)
    draw_point(ax,point3)
    #평면 그리기
    plane = three_point_plane(point1, point2, point3)
    label = draw_plane(root,ax,plane,labels,color='yellow') #새로 그린 평면 보기 좋게 노란색!
    
    return label

def add_plane(root, ax,plane1,plane2):
    plane1 = list_to_numpy(plane1)
    plane2 = list_to_numpy(plane2)

    draw_plane(root,ax,plane1)
    draw_plane(root,ax,plane2)
    angle = two_plane_angle(plane1,plane2)
    label = tk.Label(root, text=f"plane1 과 plane2 사이 각도: {angle}")
    return label

def add_plane_and_line(root,ax,s_point, n_point,u1_point,u1a_point,sp_plane):
    s_point = list_to_numpy(s_point)
    n_point = list_to_numpy(n_point)
    u1_point = list_to_numpy(u1_point)
    u1a_point = list_to_numpy(u1a_point)
    sp_plane = list_to_numpy(sp_plane)
    #plane먼저 만들기
    plane = two_point_one_plane(u1a_point,u1_point,sp_plane)
    draw_plane(root,ax,plane,"새로 그린 plane")
    draw_line(ax,u1a_point,u1_point)
    #각도 구하기
    angle = slove_line_and_plane_angle(plane,s_point,n_point)
    label = tk.Label(root, text=f"평면과 line 사이 각도: {angle}")
    return label
def add_plane_and_line2(app,ax,l1,l1a,mp_plane):
    l1 = list_to_numpy(l1)
    l1a = list_to_numpy(l1a)
    mp_plane = list_to_numpy(mp_plane)
    angle = slove_line_and_plane_angle(mp_plane,l1,l1a)
    label = tk.Label(ax, text=f"평면과 line 사이 각도: {angle}")
    return label 
   
def two_point(root, ax,point1,point2):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    draw_point(ax,point1)
    draw_point(ax,point2)
    distance = two_point_distance(point1,point2)
    label = tk.Label(root, text=f"두 점 사이 거리 : {distance}")
    return label

def point_and_plane(root,ax,point,plane):
    '''점과 평면 사이 거리 구하는 함수'''
    point = list_to_numpy(point)
    plane = list_to_numpy(plane)
    draw_plane(root,ax,plane)
    draw_point(ax,point)
    distance = point_and_plane_distance(point, plane)
    label = tk.Label(root, text=f"점과 평면 사이의 거리: {distance}")
    return label

def points_and_mid_points_plane(root,ax,orbitale_1,orbitale_2,porion_1,porion_2,plane_name):
    orbitale_1 = list_to_numpy(orbitale_1)
    orbitale_2 = list_to_numpy(orbitale_2)
    porion_1 = list_to_numpy(porion_1)
    porion_2 = list_to_numpy(porion_2)

    mid_porion = np.array([((porion_2[0]+porion_1[0])/2),(porion_2[1]+porion_1[1])/2,(porion_2[2]+porion_1[2])/2])
    draw_point(ax,orbitale_1)
    draw_point(ax,orbitale_2)
    draw_point(ax,porion_1)
    draw_point(ax,porion_2)
    draw_point(ax,mid_porion,color='green')

    #평면 그리기
    plane = three_point_plane(orbitale_1, orbitale_2, mid_porion)
    label = draw_plane(root,ax,plane,plane_name,color='green')
    
    return label

def two_point_one_plane_solve(root,ax,point1,point2,plane,plane_name):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    plane = list_to_numpy(plane)

    draw_point(ax,point1)
    draw_point(ax,point2)
    draw_plane(root,ax,plane)

    solve_plane = two_point_one_plane(point1,point2,plane)
    label = draw_plane(root,ax,solve_plane,plane_name,color='cyan')
    return label

def solve_one_point_two_plane(root, ax,point, plane1, plane2,plane_name):
    point = list_to_numpy(point)
    plane1 = list_to_numpy(plane1)
    plane2 = list_to_numpy(plane2)

    draw_point(ax,point)
    draw_plane(root,ax,plane1)
    draw_plane(root,ax,plane2)
    solve_plane = two_plane_one_point(point,plane1,plane2)
    label = draw_plane(root,ax,solve_plane,plane_name,color='green')
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

def solve_parallel_plane_point(root, ax,point,plane,plane_name):
    point = list_to_numpy(point)
    plane = list_to_numpy(plane)
    draw_plane(root,ax,plane)
    draw_point(ax,point)
    solve_plane = one_parallel_plane_and_point(plane,point)
    label = draw_plane(root,ax,solve_plane,plane_name,color='green')
    return label

def solve_three_point_angle(root,ax,point1, point2, point3):
    point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    point3 = list_to_numpy(point3)
    draw_point(ax,point1)
    draw_point(ax,point2)
    draw_point(ax,point3)
    degree = three_point_angle_solve(point1,point2,point3)
    label = tk.Label(root, text=f"세 점이 이루는 각도: {degree}")
    return label    

def solve_middle_point(root,ax,point1,point2):
    point1 =     point1 = list_to_numpy(point1)
    point2 = list_to_numpy(point2)
    draw_point(ax,point1)
    draw_point(ax,point2)
    middle_point = middle_two_point(point1=point1,point2=point2)
    draw_point(ax=ax, point=middle_point, color='green')
    label = tk.Label(root, text=f"두 점의 중간점: {middle_point}")
    return label