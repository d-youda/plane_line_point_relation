import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import plot_cube
from plane_class import two_point_middle_point_plane,SP_Plane,XZ_plane,XY_plane
from angle_class import Three_point_angle,Point_and_plane_angle,Two_Plane_Angle
from distance_class import Two_point_distance,Point_and_Plane_distance
import numpy as np

#-----체크 박스 선택 or 해제 알기 위한 global 변수-------
plane = 0
angle = 0
distance = 0
#---------------input 점들 값 받기---------------
file = '.\\1003.txt' #파일 경로
def float2intarray(list):
    result = [int(float(point)) for point in list]
    return np.array(result)

def file_extract_point(line):
    points = line.split("(")[1]
    points = points.split(",")
    result = float2intarray(points)
    return result
with open(file,"r") as f:
    while True:
        line = f.readline()
        if not line: # 파일 읽기가 종료된 경우
            break
        line = line.replace(")\n","")#필요없는 부분 제거
        point_name = line.strip().split(",")[0]
        if point_name=="N":
            N_point = np.array(file_extract_point(line))
        elif point_name=='Sella':
            S_point = np.array(file_extract_point(line))
        elif point_name=="R Or":
            OrR = np.array(file_extract_point(line))
        elif point_name == "L Or":
            OrL = np.array(file_extract_point(line))
        elif point_name == "R Po":
            PoR = np.array(file_extract_point(line))
        elif point_name == "L Po":
            PoL = np.array(file_extract_point(line))
        elif point_name == "R U1CP":
            U1R = np.array(file_extract_point(line))
        elif point_name == "L U1CP":
            U1L = np.array(file_extract_point(line))
        elif point_name == "R U1RP":
            U1RA = np.array(file_extract_point(line))
        elif point_name == "L U1RP":
            U1LA = np.array(file_extract_point(line))
        elif point_name =="R U6CP":
            U6R = np.array(file_extract_point(line))
        elif point_name == "L U6CP":
            U6L = np.array(file_extract_point(line))
        elif point_name=="R L1CP":
            L1R = np.array(file_extract_point(line))
        elif point_name=="R L1RP":
            L1AR = np.array(file_extract_point(line))
        elif point_name=='A':
            A_point = np.array(file_extract_point(line))
        elif point_name=='B':
            B_point = np.array(file_extract_point(line))
        elif point_name=='Pog':
            POG = np.array(file_extract_point(line))
#점 직접 입력받기
# N_point = np.array([110.21, 38.49, 140.01])
# N_point = float2intarray(N_point)
            
# S_point = np.array([110.83, 102.22, 125.53])
# S_point = float2intarray(S_point)
            
# OrR = np.array([80.18, 43.88, 110.84])
# OrR = float2intarray(OrR)
            
# OrL =  np.array([143.26, 42.59, 116.96])
# OrL = float2intarray(OrL)
            
# PoR = np.array([52.76, 126.27, 100.49])
# PoR = float2intarray(PoR)
            
# PoL = np.array([175.38, 121.21, 113.86])
# PoL = float2intarray(PoL)
            
# U1R = np.array([109.51, 21.69, 58.92])
# U1R = float2intarray(U1R)
            
# U1L = np.array([119.53, 22.09, 58.66])
# U1L = float2intarray(U1L)
            
# U1RA = np.array([110.59, 34.82, 79.23])
# U1RA = float2intarray(U1RA)
            
# U1LA = np.array([117.85, 34.17, 79.59])
# U1LA = float2intarray(U1LA)
            
# U6R = np.array([86.22, 51.1, 60.31])
# U6R = float2intarray(U6R)
            
# U6L = np.array([141.24, 54.31, 63.73])
# U6L = float2intarray(U6L)
            
# L1R = np.array([106.31, 21.26, 58.86])
# L1R = float2intarray(L1R)
            
# L1AR = np.array([104.83, 29.26, 39.19])
# L1AR = float2intarray(L1AR)
            
# A_point = np.array([113.57, 31.2, 81.36])
# A_point = float2intarray(A_point)
            
# B_point = np.array([107.68, 25.39, 37.77])
# B_point = float2intarray(B_point)
            
# POG = np.array([107.23, 23.73, 24.2])
# POG = float2intarray(POG)

root = tk.Tk() #tk 객체 생성
#---------------checkbutton의 event함수들 정의---------------
def plane_cb_event():
    global plane
    if plane == 0:
        FH_Plane_button.pack()
        OP_Plane_button.pack()
        SP_plane_button.pack()
        XZ_plane_button.pack()
        XY_plane_button.pack()
        plane +=1 
    elif plane == 1:
        FH_Plane_button.pack_forget()
        OP_Plane_button.pack_forget()
        SP_plane_button.pack_forget()
        XZ_plane_button.pack_forget()
        XY_plane_button.pack_forget()
        plane = 0
def angle_ck_event():
    global angle
    if angle==0:
        three_point_angle1.pack()
        three_point_angle2.pack()
        three_point_angle3.pack()
        point_and_plane_angle1.pack()
        plane_and_plane_angle.pack()
        angle += 1
    elif angle==1:
        three_point_angle1.pack_forget()
        three_point_angle2.pack_forget()
        three_point_angle3.pack_forget()
        point_and_plane_angle1.pack_forget()
        plane_and_plane_angle.pack_forget()
        angle = 0
def distnace_ck_event():
    global distance
    if distance==0:
        point_distance1.pack()
        point_distance2.pack()
        point_and_plane_distance1.pack()
        point_and_plane_distance2.pack()
        point_and_plane_distance3.pack()
        distance += 1
    elif distance==1:
        point_distance1.pack_forget()
        point_distance2.pack_forget()
        point_and_plane_distance1.pack_forget()
        point_and_plane_distance2.pack_forget()
        point_and_plane_distance3.pack_forget()
        distance = 0
def delete():
            ax.clear()
            plot_cube(ax)
            canvas.draw()
#---------------radio button의 event함수들 정의---------------
#평면 구해서 canvas에 그리기
def fh_plane_event():
    solve_FH_Plane.plot()
def op_plane_event():
    OP_plane.plot()
def sp_plane_event():
    solve_SP_plane.plot()
def XZ_plane_event():
    solve_XZ_plane.plot()
def xy_plane_event():
    solve_xy_plane.plot()

#angle값 밑에 찍어주고, canvas에 도형 그리기
def sna_event():
        sna.draw_event()
def snb_event():
     snb.draw_event()
def anb_event():
     anb.draw_event()
def u1_sn_event():
     u1sn.draw_event()
def op_fh_angle_event():
     op_fh_angle.draw_event()
    
#distance 밑에 찍어주고, canvas에 도형 그리기
def overjet_event():
     overjet.draw_event()
def overbite_event():
     overbite.draw_event()
def u1z_event():
     u1z.draw_event()
def a_z_event():
     a_z.draw_event()
def pog_z_event():
     pog_z.draw_event()
#---------------3d cube 그리기---------------
fig = plt.Figure(figsize=(5, 5), tight_layout=True) #3d cube 그릴 캔버스 생성
ax = fig.add_subplot(111, projection='3d') #canvas 3D로 변경
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) #캔버스 화면 좌측에 고정시키기
plot_cube(ax) #cube 그리기

#---------------해당 연산과 관련된 radio button 보여줄checkbutton---------------
plane_ckbutton = tk.Checkbutton(root, text="평면 구하기",command=plane_cb_event)
plane_ckbutton.pack()
angle_ckbutton = tk.Checkbutton(root, text="각도 구하기",command=angle_ck_event)
angle_ckbutton.pack()
distance_ckbutton = tk.Checkbutton(root, text="거리 구하기",command=distnace_ck_event)
distance_ckbutton.pack()
delete_button = tk.Button(root, text="plot reset",command=delete,height=5,width=10,bg='red',fg='white')
delete_button.pack(side=tk.BOTTOM,pady=10)
#---------------평면 구하기---------------
plane_value = tk.IntVar()
solve_FH_Plane = two_point_middle_point_plane(canvas=canvas, ax=ax, root=root,
                                        point1=OrR,point2=OrL,middle_point1=PoR, middle_point2=PoL,
                                        label='FH plane',color='yellow')
FH_Plane_button = tk.Radiobutton(root,text="FH 평면 구하기",value=1,command=fh_plane_event,variable=plane_value)
FH_plane = solve_FH_Plane.plane()
FH_Plane_button.pack_forget()

OP_plane = two_point_middle_point_plane(canvas=canvas,ax=ax,root=root,
                                        point1=U6L,point2=U6R,middle_point1=U1R,middle_point2=U1L,
                                        label='OP plane',color='green')
op_plane = OP_plane.plane()
OP_Plane_button = tk.Radiobutton(root, text='OP 평면 구하기',value=2,command=op_plane_event,variable=plane_value)
OP_Plane_button.pack_forget()

solve_SP_plane = SP_Plane(canvas=canvas,ax=ax,root=root,
                          n_point=N_point, s_point=S_point,FH_plane=FH_plane,
                          label='SP plane', color='skyblue')
sp_plane = solve_SP_plane.plane()
SP_plane_button = tk.Radiobutton(root, text='SP 평면 구하기',value=3,command=sp_plane_event,variable=plane_value)
SP_plane_button.pack_forget()

solve_XZ_plane = XZ_plane(canvas=canvas, ax=ax,root=root,
                          FH_plane=FH_plane,n_point=N_point,
                          label='XZ plane', color='violet')
XZ_plane_button = tk.Radiobutton (root, text='XZ 평면 구하기',value=4,command=XZ_plane_event,variable=plane_value)
XZ_plane_button.pack_forget()

solve_xy_plane = XY_plane(canvas=canvas, ax=ax, root=root,
                          FH_plane=FH_plane, SP_plane=sp_plane,n_point=N_point,
                          label='xy plane', color='yellowgreen')
coronal_plane = solve_xy_plane.plane()
XY_plane_button = tk.Radiobutton(root, text='XY 평면 구하기',value=5,command=xy_plane_event,variable=plane_value)
XY_plane_button.pack_forget()

#---------------각도 구하기---------------
angle_value = tk.IntVar()
sna = Three_point_angle(canvas=canvas, ax=ax, root=root,
                        point1=S_point, point2=N_point, point3=A_point,
                        label='SNA')
three_point_angle1 = tk.Radiobutton(root,text="SNA", value=1, command=sna_event,variable=angle_value)
three_point_angle1.pack_forget()
snb = Three_point_angle(canvas=canvas, ax=ax, root=root,
                        point1=S_point, point2=N_point, point3=B_point,
                        label='SNB')
three_point_angle2 = tk.Radiobutton(root,text="SNB", value=2, command=snb_event,variable=angle_value)
three_point_angle2.pack_forget()
anb = Three_point_angle(canvas=canvas, ax=ax, root=root,
                        point1=A_point, point2=N_point, point3=B_point,
                        label='ANB')
three_point_angle3 = tk.Radiobutton(root,text="ANB", value=3, command=anb_event,variable=angle_value)
three_point_angle3.pack_forget()
solve_sn_plane = SP_Plane(canvas=canvas,ax=ax,root=root,
                    n_point=N_point,s_point=S_point,FH_plane=sp_plane,
                    label="SN plane",color='purple') #U1-SN에 필요한 Sn plane 구하기
sn_plane = solve_sn_plane.plane()
u1sn = Point_and_plane_angle(canvas=canvas,ax=ax,root=root,
                             point1=U1R,point2=U1RA,plane=sn_plane,label='U1-SN')
point_and_plane_angle1 = tk.Radiobutton(root,text="U1-SN", value=4, command=u1_sn_event,variable=angle_value)
point_and_plane_angle1.pack_forget()
# lmpa = Point_and_plane_angle(canvas=canvas,ax=ax,root=root,
#                              point1=L1R,point2=U1RA,plane=sn_plane,label='1MPA')
# point_and_plane_angle2 = tk.Radiobutton(root,text="1MPA", value=5, command=None,variable=angle_value)
# point_and_plane_angle2.pack()

op_fh_angle = Two_Plane_Angle(canvas=canvas, ax=ax, root=root,
                              plane1=op_plane,plane2=FH_plane,label='OP-FH')
plane_and_plane_angle = tk.Radiobutton(root,text="OP-FH", value=6, command=op_fh_angle_event,variable=angle_value)
plane_and_plane_angle.pack_forget()

#---------------거리 구하기---------------
overjet = Two_point_distance(root=root, canvas=canvas,ax=ax,
                             point1=U1R,point2=L1R,label="overjet")
point_distance1 = tk.Radiobutton(root,text="Overjet", value=7, command=overjet_event,variable=angle_value)
point_distance1.pack_forget()

overbite = Two_point_distance(root=root, canvas=canvas,ax=ax,
                             point1=U1R,point2=L1R,label="overbite")
point_distance2 = tk.Radiobutton(root,text="Overbite", value=8, command=overbite_event,variable=angle_value)
point_distance2.pack_forget()

u1z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=U1R,plane=coronal_plane,label='U1-Z')
point_and_plane_distance1 = tk.Radiobutton(root,text="U1-Z", value=9, command=u1z_event,variable=angle_value)
point_and_plane_distance1.pack_forget()

a_z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=A_point,plane=coronal_plane,label='A-Z')
point_and_plane_distance2 = tk.Radiobutton(root,text="A-Z", value=10, command=a_z_event,variable=angle_value)
point_and_plane_distance2.pack_forget()

pog_z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=POG,plane=coronal_plane,label='Pog-Z')
point_and_plane_distance3 = tk.Radiobutton(root,text="Pog-Z", value=11, command=pog_z_event,variable=angle_value)
point_and_plane_distance3.pack_forget()

root.mainloop()