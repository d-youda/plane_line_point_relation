from math_method.point import two_point_distance,point_and_plane_distance
from button import draw_point,draw_plane
import tkinter as tk
class Two_point_distance():
    def __init__(self,root,canvas,ax,point1,point2,label):
        self.root = root
        self.canvas = canvas
        self.ax = ax
        self.point1 = point1
        self.point2 = point2
        self.label = label

    def distance(self):
        distances = two_point_distance(point1=self.point1,point2=self.point2)
        return distances
    
    def draw_event(self):
        draw_point(ax=self.ax, point=self.point1)
        draw_point(ax=self.ax, point=self.point2, color='green')
        distance_label = tk.Label(self.root, text=f"{self.label} 거리: {self.distance()}")
        distance_label.pack()
        self.canvas.draw()

class Point_and_Plane_distance():
    def __init__(self,root,canvas,ax,point,plane,label):
        self.root = root
        self.canvas = canvas
        self.ax = ax
        self.point = point
        self.plane = plane
        self.label = label
    
    def distance(self):
        distances = point_and_plane_distance(point=self.point, plane=self.plane)
        return distances
    
    def draw_event(self):
        distance_label = tk.Label(self.root, text=f"{self.label} 거리: {self.distance()}")
        distance_label.pack()
        draw_point(ax=self.ax, point=self.point)
        draw_plane(root=self.root, ax=self.ax, plane=self.plane,label='Coronal')
        self.canvas.draw()