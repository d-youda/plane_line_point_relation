import tkinter as tk
from button import add_point,add_plane,add_plane_and_line,two_point,point_and_plane,points_and_mid_points_plane,two_point_one_plane_solve,solve_one_point_two_plane,solve_two_lines_angle
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
            line_dir_vec = line_dir_vec_entry.get().split(",")
            angle = add_plane_and_line(root,ax,plane,line_point1,line_dir_vec)
            angle.pack(side=tk.BOTTOM, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for plane1, or plane2")
    label = tk.Label(root, text="각도를 구할 라인과 평면을 입력하세요")
    label.pack(side=tk.TOP,pady=5)
    label1 = tk.Label(root, text="평면을 먼저 입력하세요(ax+by+cz=0)")
    label1.pack(side=tk.TOP,pady=5)
    plane_entry = entry_label(root, "a,b,c")
    label2 = tk.Label(root, text='직선이 지나가는 한 점(x,y,z)과 방향벡터(a,b,c)를 입력하세요')
    label2.pack(side=tk.TOP,pady=5)
    line_point1_entry = entry_label(root, "x,y,z")
    line_dir_vec_entry = entry_label(root, "a,b,c")

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

def point_and_mid_point_plane(root,ax,canvas):
    def point_mid_point_plane(ax=ax, canvas=canvas):
        try:
            orbitale_1 = orbitale_entry_1.get().split(",")
            orbitale__2 = orbitale_entry_2.get().split(",")
            porion_1 = portion_entry_1.get().split(",")
            porion_2 = portion_entry_2.get().split(",")
            
            label = points_and_mid_points_plane(root,ax,orbitale_1,orbitale__2,porion_1,porion_2)
            label.pack(side=tk.TOP, pady=5)
            canvas.draw()
        except ValueError:
            print("Invalid input for point or plane")     
    label = tk.Label(root, text="좌/우 orbitale 두 점과 좌/우 portion 두 점을 입력하세요")
    label.pack(side=tk.TOP,pady=5)
    
    label_orbitale = tk.Label(root, text="좌/우orbitale의 각각 점을 입력하세요(x,y,z)")
    label_orbitale.pack(side=tk.TOP, pady=5)
    orbitale_entry_1 = entry_label(root, "x1,y1,z1")
    orbitale_entry_2 = entry_label(root, "x2,y2,z2")

    label_portion = tk.Label(root, text="portion 두 점을 각각 입력하세요")
    label_portion.pack(side=tk.TOP,pady=5)
    portion_entry_1 = entry_label(root, "x1,y1,z1")
    portion_entry_2 = entry_label(root, "x2,y2,z2")

    button_add_plane = tk.Button(root, text="Calculate distance and add figure!", command=point_mid_point_plane)
    button_add_plane.pack(pady=10)

def two_points_one_plane(root,ax,canvas):
    def slove_two_point_one_plane(ax=ax,canvas=canvas):
        point1 = point1_entry.get().split(",")
        point2 = point2_entry.get().split(",")
        plane = plane_entry.get().split(",")

        label = two_point_one_plane_solve(root,ax,point1,point2,plane)
        label.pack(side=tk.TOP,pady=5)
        canvas.draw()
    label = tk.Label(root, text="두 점을 지나며, 한 평면에 수직인 평면을 구해보겠습니다. 두 점을 먼저 입력해주세요")
    label.pack(side=tk.TOP, pady=5)

    point1_entry = entry_label(root,"x,y,z")
    point2_entry = entry_label(root,"x,y,z")

    plane_label = tk.Label(root, text="수직이 될 한 평면을 입력하세요(ax+by+cz=d)")
    plane_label.pack(side=tk.TOP, pady=5)
    plane_entry = entry_label(root, "a,b,c,d")
    button_add_plane = tk.Button(root, text="Calculate distance and add figure!", command=slove_two_point_one_plane)
    button_add_plane.pack(pady=10)

def one_point_two_planes(root,ax,canvas):
    def one_point_two_plane(ax=ax, canvas=canvas):
        point = point_entry.get().split(",")
        plane1 = plane1_entry.get().split(",")
        plane2 = plane2_entry.get().split(",")

        label = solve_one_point_two_plane(root,ax,point,plane1,plane2)
        label.pack(side=tk.TOP,pady=5)
        canvas.draw()

    label = tk.Label(root, text='한 점을 지나면서, 두 평면과 수직인 평면을 구해보겠습니다. 한 점을 먼저 입력하세요.')
    label.pack(side=tk.TOP, pady=5)

    point_entry = entry_label(root,"x,y,z")
    point_entry.pack(side=tk.TOP, pady=5)

    plane_label = tk.Label(root, text="평면을 입력해주세요(ax+by+cz=d)")
    plane_label.pack(side=tk.TOP,pady=5)
    plane1_entry = entry_label(root,"a,b,c,d")
    plane2_entry = entry_label(root,"a,b,c,d")
    plane1_entry.pack(side=tk.TOP,pady=5)
    plane2_entry.pack(side=tk.TOP,pady=5)

    button_add_plane = tk.Button(root, text="Calculate distance and add figure!", command=one_point_two_plane)
    button_add_plane.pack(pady=10)

def line_and_line_angle(root,ax,canvas):
    def line_and_line_angles(ax=ax, canvas=canvas):
        line1_point = line1_point_entry.get().split(",")
        line1_dir_vec = line1_dir_vec_entry.get().split(",")
        line2_point = line2_point_entry.get().split(",")
        line2_dir_vec = line2_dir_vec_entry.get().split(",")
        label = solve_two_lines_angle(root,ax,line1_point, line1_dir_vec, line2_point, line2_dir_vec)
        label.pack(side=tk.TOP,pady=5)
        canvas.draw()        
    label = tk.Label(root, text="두 직선의 각도를 구해보겠습니다. 각 직선이 출발할 점과, 방향벡터를 입력하세요")
    label.pack(side=tk.TOP, pady=5)
    line1_point_entry = entry_label(root,"x,y,z")
    line1_dir_vec_entry = entry_label(root,"a,b,c")

    line2_point_entry = entry_label(root,"x,y,z")
    line2_dir_vec_entry = entry_label(root,"a,b,c")

    line1_point_entry.pack(side=tk.TOP, pady=5)
    line2_point_entry.pack(side=tk.TOP, pady=5)
    line1_dir_vec_entry.pack(side=tk.TOP, pady=5)
    line2_dir_vec_entry.pack(side=tk.TOP, pady=5)

    button_add_plane = tk.Button(root, text="Calculate distance and add figure!", command=line_and_line_angles)
    button_add_plane.pack(pady=10)