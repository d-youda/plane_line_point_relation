import tkinter as tk
from button import three_points_plane,add_plane,add_plane_and_line,two_point,point_and_plane,points_and_mid_points_plane,two_point_one_plane_solve,solve_one_point_two_plane,solve_two_lines_angle,solve_parallel_plane_point,solve_three_point_angle,solve_middle_point,add_plane_and_line2
# from text_label import entry_label
from math_method.plane import two_plane_angle
def point_make_plane(root,ax,canvas,entry_point1,entry_point2,entry_point3,plane_name):
    try:
        point1 = entry_point1.get().split(",")
        point2 = entry_point2.get().split(",")
        point3 = entry_point3.get().split(",")
        eq_label = three_points_plane(root,ax,point1,point2,point3,labels=plane_name)

        eq_label.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1, point2, or point3")

def make_fh_plane(app,ax,canvas,fh_entry1,fh_entry2,fh_entry3,fh_entry4,plane_name):
    try:
        point1 = fh_entry1.get().split(",")
        point2 = fh_entry2.get().split(",")
        point3 = fh_entry3.get().split(",")
        point4 = fh_entry4.get().split(",")
        plane_label = points_and_mid_points_plane(app,ax,point1,point2,point3,point4,plane_name)
        plane_label.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1, point2, or point3")

def make_sp_plane(app,ax,canvas,sp_n_entry,sp_s_entry,sp_plane_entry,plane_name = 'SP 평면'):
    try:
        n_point = sp_n_entry.get().split(",")
        s_point = sp_s_entry.get().split(",")
        sp_plane = sp_plane_entry.get().split(",")
        plane_label = two_point_one_plane_solve(app,ax,n_point,s_point,sp_plane,plane_name)
        plane_label.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1, point2, or point3")

def make_xz_plane(app,ax,canvas,plane_entry,n_point_entry,plane_name='XZ 평면'):
    try:
        fh_plane = plane_entry.get().split(",")
        n_point = n_point_entry.get().split(",")
        plane_label = solve_parallel_plane_point(app,ax,n_point,fh_plane,plane_name)
        plane_label.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1, plane")

def make_xy_plane(app,ax,canvas,fh_plane_entry,sp_plane_entry,n_point_entry,plane_name="XY 평면"):
    try:
        fh_plane = fh_plane_entry.get().split(",")
        sp_plane = sp_plane_entry.get().split(",")
        n_point = n_point_entry.get().split(",")
        plane_label = solve_one_point_two_plane(app,ax,n_point,fh_plane,sp_plane,plane_name)
        plane_label.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1 or two plane")

def slove_three_point_angle(app,ax,canvas,point1_entry,point2_entry,point3_entry):
    try:
        point1 = point1_entry.get().split(",")
        point2 = point2_entry.get().split(",")
        point3 = point3_entry.get().split(",")
        angle = solve_three_point_angle(app,ax,point1,point2,point3)
        angle.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")

def solve_plane_and_line_angle(app,ax,canvas,u1_point_entry,u1a_point_entry,s_point_entry,n_point_entry,sp_plane_entry2,plane_name="SP 평면"):
    try:
        u1_point = u1_point_entry.get().split(",")
        u1a_point = u1a_point_entry.get().split(",")
        s_point = s_point_entry.get().split(",")
        n_point = n_point_entry.get().split(",")
        sp_plane = sp_plane_entry2.get().split(",")
        angle = add_plane_and_line(app,ax,s_point, n_point,u1_point,u1a_point,sp_plane)
        angle.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")

def solve_plane_and_line_angle2(app,ax,canvas,l1,l1a,mp_plane):
    try:
        l1 = l1.get().split(",")
        l1a = l1a.get().split(",")
        mp_plane = mp_plane.get().split(",")
        angle = add_plane_and_line2(app,ax,l1,l1a,mp_plane)
        angle.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")

def solve_two_plane_angle(app,ax,canvas,op_plane,fh_plane):
    try:
        op_plane = op_plane.get().split(",")
        fh_plane = fh_plane.get().split(",")
        angle = add_plane(app,ax,op_plane,fh_plane)
        angle.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")

def solve_two_point_distance(app,ax,canvas,point1,point2):
    try:
        point1 = point1.get().split(",")
        point2 = point2.get().split(",")
        distance = two_point(app,ax, point1,point2)
        distance.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")

def solve_point_and_plane_distance(app,ax,canvas,button12_point,button12_plane):
    try:
        point = button12_point.get().split(",")
        plane = button12_plane.get().split(",")
        distance = point_and_plane(app,ax,point,plane)
        distance.pack()
        canvas.draw()
    except ValueError:
        print("Invalid input for point1,point2 or point3")