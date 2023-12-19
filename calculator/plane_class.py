from math_method.point import middle_two_point
from math_method.plane import three_point_plane, two_point_one_plane,one_parallel_plane_and_point,two_plane_one_point
from button import draw_plane,draw_point
import numpy as np
import tkinter as tk
class two_point_middle_point_plane():
    '''
    두 점의 중간 점과, 다른 두 점을 지나는 평면 구하는 클래스
    '''
    def __init__(self,canvas,ax,root,point1,point2,middle_point1,middle_point2,label,color):
        #세 점
        self.point1 = point1
        self.point2 = point2
        #중간 점 구하기
        self.middle_point = middle_two_point(point1=middle_point1, point2=middle_point2) 
        self.ax = ax
        self.root = root
        self.canvas = canvas
        self.label = label
        self.color = color

    def plane(self):
        #enldptj 
        plane = three_point_plane(point1=self.point1, point2=self.point2,point3=self.middle_point)
        return plane
    
    def plot(self):
        draw_point(self.ax,point=self.point1)
        draw_point(self.ax,point=self.point2)
        draw_point(self.ax,point=self.middle_point)
        A,B,C,D = self.plane()
        plane = np.array([A,B,C,D])
        label = draw_plane(root=self.root,ax=self.ax,plane=plane,
                           label=f'{self.label}', color=self.color)
        label.pack()
        self.canvas.draw()

class SP_Plane():
    '''
    SP 평면을 구하는 클래스
    '''
    def __init__(self,canvas,ax,root,n_point,s_point,FH_plane,label,color):
        self.n_point = n_point
        self.s_point = s_point
        self.FH_plane = FH_plane
        self.ax = ax
        self.root = root
        self.canvas = canvas
        self.label = label
        self.color = color
    
    def plane(self):
        plane = two_point_one_plane(point1=self.n_point, point2=self.s_point,plane=self.FH_plane)
        return plane
    
    def plot(self):
        draw_point(ax=self.ax, point=self.n_point)
        draw_point(ax=self.ax, point=self.s_point)
        #새 plane 그리기
        A,B,C,D = self.plane()
        plane = np.array([A,B,C,D])
        label = draw_plane(root=self.root,ax=self.ax,plane=plane,
                           label=f'{self.label}', color=self.color,vertical=True)
        label.pack()
        self.canvas.draw()

class XZ_plane():
    def __init__(self,canvas,ax,root,FH_plane, n_point,label,color):
        self.canvas = canvas
        self.ax = ax
        self.root = root
        self.FH_plane = FH_plane
        self.n_point = n_point
        self.label = label
        self.color = color
    def plane(self):
        plane = one_parallel_plane_and_point(plane=self.FH_plane, point=self.n_point)
        return plane
    
    def plot(self):
        draw_point(ax=self.ax, point=self.n_point)
        A,B,C,D = self.plane()
        plane = np.array([A,B,C,D])
        label = draw_plane(root=self.root,ax=self.ax,plane=plane,
                           label=f'{self.label}', color=self.color)
        label.pack()
        self.canvas.draw()

class XY_plane():
    def __init__(self,canvas,ax,root,FH_plane,SP_plane,n_point,label,color):
        self.canvas = canvas
        self.ax = ax
        self.root = root
        self.FH_plane = FH_plane
        self.SP_plane = SP_plane
        self.n_point = n_point
        self.label = label
        self.color = color

    def plane(self):
        plane = two_plane_one_point(point=self.n_point, plane1=self.FH_plane, plane2=self.SP_plane)
        return plane
    
    def plot(self):
        draw_point(ax=self.ax, point=self.n_point)
        A,B,C,D = self.plane()
        plane = np.array([A,B,C,D])
        label = draw_plane(root=self.root,ax=self.ax,plane=plane,
                           label=f'{self.label}', color=self.color,vertical=True)
        label.pack()
        self.canvas.draw()