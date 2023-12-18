import numpy as np
import math_method.point as point
import math_method.line as line
from math_method.plane import two_plane_angle
import tkinter as tk
from button import draw_point, draw_line,draw_plane
class Three_point_angle():
    def __init__(self,canvas,ax,root,point1,point2,point3,label):
        self.canvas = canvas
        self.ax = ax
        self.root = root
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.label = label

    def angle(self):
        angle = point.three_point_angle_solve(point1=self.point1,point2=self.point2, point3=self.point3)
        return angle
    
    def draw_event(self):
        angle_label = tk.Label(self.root, text=f"{self.label} 각도:{self.angle()}")
        angle_label.pack()
        draw_point(ax=self.ax,point=self.point1,color='red')
        draw_point(ax=self.ax,point=self.point2,color='green')
        draw_point(ax=self.ax,point=self.point3,color='blue')
        self.canvas.draw()

class Point_and_plane_angle():
    def __init__(self,canvas,ax,root,point1,point2,plane,label):
        self.canvas = canvas
        self.ax = ax
        self.root = root
        self.point1 = point1
        self.point2 = point2
        self.plane = plane
        self.label = label

    def angle(self):
        angle = line.slove_line_and_plane_angle(plane=self.plane, line_point1=self.point1,line_point2=self.point2)
        return angle
    
    def draw_event(self):
        angle_label = tk.Label(self.root, text=f"{self.label} 각도:{self.angle()}")
        angle_label.pack()
        draw_point(ax=self.ax,point=self.point1,color='red')
        draw_point(ax=self.ax,point=self.point2,color='blue')
        draw_line(ax=self.ax, point1=self.point1,point2=self.point2)
        draw_plane(root=self.root, ax=self.ax,plane=self.plane,label='SN plane')
        self.canvas.draw()

class Two_Plane_Angle():
    def __init__(self,canvas,ax,root,plane1,plane2,label):
        self.canvas = canvas
        self.ax = ax
        self.root = root
        self.plane1 = plane1
        self.plane2 = plane2
        self.label = label
    def angle(self):
        angle = two_plane_angle(plane1=self.plane1, plane2=self.plane2)
        return angle
    
    def draw_event(self):
        angle_label = tk.Label(self.root, text=f"{self.label} 각도:{self.angle()}")
        angle_label.pack()
        draw_plane(root=self.root,ax=self.ax,plane=self.plane1,label='OP plane')
        draw_plane(root=self.root,ax=self.ax,plane=self.plane2,label='OP plane',color='yellow')
        self.canvas.draw()