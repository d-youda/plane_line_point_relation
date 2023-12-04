import tkinter as tk
from button import add_point,add_plane,add_plane_and_line,two_point,point_and_plane
from text_label import entry_label
from math_method.plane import two_plane_angle
def three_point_make_plane(root,ax,canvas):
    def point_make_plane(ax=ax,canvas=canvas):
        try:
            point1 = entry_point1.get().split(",")
            point2 = entry_point2.get().split(",")
            point3 = entry_point3.get().split(",")
            eq_label = add_point(root,ax,point1,point2,point3)
            eq_label.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for point1, point2, or point3")

    #entry 만들기
    label = tk.Label(root, text="세 점을 입력하세요")
    label.pack(side=tk.TOP, pady=5)
    entry_point1 = entry_label(root, "x,y,z:")
    entry_point2 = entry_label(root, "x,y,z:")
    entry_point3 = entry_label(root, "x,y,z:")

    #세 점의 좌표 찍기
    button_add_point = tk.Button(root, text="Add point", command=point_make_plane)
    button_add_point.pack(pady=10)

def two_plane_angles(root,ax,canvas):
    def point_make_plane(ax=ax,canvas=canvas):
        try:
            plane1 = first_plane_entry.get().split(",")
            plane2 = second_plane_entry.get().split(",")

            angle = add_plane(root,ax,plane1,plane2)
            angle.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for plane1, or plane2")

    label = tk.Label(root, text="각도를 구할 두 평면을 입력하세요(ax+by+cz=0)")
    label.pack(side=tk.TOP,pady=5)
    first_plane_entry = entry_label(root, "a,b,c: ")
    second_plane_entry = entry_label(root,"a,b,c:")

    button_add_plane = tk.Button(root, text="Calculate angle and add plane!", command=point_make_plane)
    button_add_plane.pack(pady=10)

def plane_and_line_angle(root,ax,canvas):
    def plane_and_line(ax=ax,canvas=canvas):
        try:
            plane = plane_entry.get().split(",")
            line_point1 = line_point1_entry.get().split(",")
            line_point2 = line_point2_entry.get().split(",")
            angle = add_plane_and_line(root,ax,plane,line_point1,line_point2)
            angle.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for plane1, or plane2")
    label = tk.Label(root, text="각도를 구할 라인과 평면을 입력하세요")
    label.pack(side=tk.TOP,pady=5)
    label1 = tk.Label(root, text="평면을 먼저 입력하세요(ax+by+cz=0)")
    label1.pack(side=tk.TOP,pady=5)
    plane_entry = entry_label(root, "a,b,c")
    label2 = tk.Label(root, text='직선이 지나가는 두 점을 입력해주세요(x,y,z)')
    label2.pack(side=tk.TOP,pady=5)
    line_point1_entry = entry_label(root, "x,y,z")
    line_point2_entry = entry_label(root, "x,y,z")

    button_add_plane = tk.Button(root, text="Calculate angle and add figure!", command=plane_and_line)
    button_add_plane.pack(pady=10)

def two_points_distance(root, ax, canvas):
    def two_point_dis(ax=ax, canvas=canvas):
        try:
            point1 = point1_entry.get().split(",")
            point2 = point2_entry.get().split(",")
            distance_label = two_point(root,ax,point1,point2)
            distance_label.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for point1 or point2")
    label = tk.Label(root, text="거리를 구할 두 점을 입력하세요")
    label.pack(side=tk.TOP, pady=5)
    point1_entry = entry_label(root,"x,y,z")
    point2_entry = entry_label(root,"x,y,z")

    button_add_plane = tk.Button(root, text="Calculate distance and add points!", command=two_point_dis)
    button_add_plane.pack(pady=10)

def point_and_plane_distance(root, ax, canvas):
    '''점과 평면 사이 거리 구하여, 3D canvas에 나타내는 함수'''
    def point_plane_distance(ax=ax, canvas=canvas):
        try:
            point = point_entry.get().split(",")
            plane = plane_entry.get().split(",")
            distance = point_and_plane(root,ax,point,plane)
            distance.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for point or plane")            
    label = tk.Label(root, text="거리를 구할 점과 평면을 입력하세요")
    label.pack(side=tk.TOP, pady=5)
    
    label_point = tk.Label(root, text="거리를 구하기 위한 점을 먼저 입력해주세요(x,y,z)")
    label_point.pack(side=tk.TOP, pady=5)
    point_entry = entry_label(root, "x,y,z")

    label_plane = tk.Label(root, text="거리 구하기 위한 평면 입력해주세요(ax+by+cz=0)")
    label_plane.pack(side=tk.TOP, pady=5)
    plane_entry = entry_label(root, "a,b,c")

    button_add_plane = tk.Button(root, text="Calculate distance and add figure!", command=point_plane_distance)
    button_add_plane.pack(pady=10)