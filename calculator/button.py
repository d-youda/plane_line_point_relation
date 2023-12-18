import tkinter as tk
import numpy as np
from matplotlib.lines import Line2D
    
def draw_plane(root,ax,plane,label=None,color='blue',vertical=False):
    '''평면 그리는 함수'''
    if vertical:
        x, y = np.meshgrid(range(-50, 70), range(-50, 70)) #10x10 array 두 개
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
