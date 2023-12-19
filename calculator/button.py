import tkinter as tk
import numpy as np
from matplotlib.lines import Line2D
from math_method.plane import three_point_plane
from sympy import symbols, solve,Symbol
i = 0
def draw_plane(root,ax,plane,label=None,color='blue',vertical=False):
    max = 500
    global i
    '''평면 그리는 함수'''
    x, y = np.meshgrid(range(-max, max), range(-max, max)) #10x10 array 두 개
    # if vertical:
    #     x, y = np.meshgrid(range(0, 120), range(0, 120)) #10x10 array 두 개
    a,b,c,d = plane
    z = (d-a*x - b*y)/c
    z1 = np.where(z<-(max+100),None,z)
    z2 = np.where(z>(max+100),None,z1)
    
    ax.plot_surface(x,y,z2,label=f'{label}',color=color,alpha=0.7)
    legend_elements = [Line2D([0], [i], color=color, lw=2, label=f'{label}')]
    i += 1
    legend = ax.legend(handles=legend_elements)
    ax.add_artist(legend)
    label = tk.Label(root, text="%s : %.2fx + %.2fy + %.2fz = %.2f"%(label,a,b,c,d))        
    return label

def draw_point(ax,point,color='red'):
    '''점 그리는 함수'''
    ax.scatter(point[0],point[1],point[2],color=color, s=10, marker='o')

def draw_line(ax,point1,point2):
    '''직선 그리는 함수'''
    ax.plot((point1[0],point2[0]),(point1[1],point2[1]),(point1[2],point2[2]),color='green')
