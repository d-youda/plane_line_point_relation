import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from cube import plot_cube
from plane_class import two_point_middle_point_plane,SP_Plane,XZ_Plane,XY_Plane
from angle_class import Three_point_angle,Point_and_plane_angle,Two_Plane_Angle
from distance_class import Two_point_distance,Point_and_Plane_distance
import numpy as np
import tkinter.messagebox as msgbox
from input_text import input_file
from button import draw_plane

#-----체크 박스 선택 or 해제 알기 위한 global 변수-------
plane = 0
angle = 0
distance = 0
fh_plane = 0
op_plane = 0
sp_plane = 0
coronal_plane = 0

N_point = np.array([0,0,0])
S_point = np.array([0,0,0])
OrR = np.array([0,0,0])
OrL = np.array([0,0,0])
PoR = np.array([0,0,0])
PoL=np.array([0,0,0])
U1R=np.array([0,0,0])
U1L=np.array([0,0,0])
U1RA=np.array([0,0,0])
U1LA=np.array([0,0,0])
U6R=np.array([0,0,0])
U6L=np.array([0,0,0])
L1R=np.array([0,0,0])
L1AR=np.array([0,0,0])
A_point=np.array([0,0,0])
B_point=np.array([0,0,0])
POG = np.array([0,0,0])

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
        fh_plane
        OP_Plane_button.pack_forget()
        SP_plane_button.pack_forget()
        XZ_plane_button.pack_forget()
        XY_plane_button.pack_forget()

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
#----------------button event 함수들---------------
def input_file_event():
    file = filedialog.askopenfilename()
    global N_point,S_point,OrR,OrL,PoR,PoL,U1R,U1L,U1RA,U1LA,U6R,U6L,L1R,L1AR,A_point,B_point,POG
    N_point,S_point,OrR,OrL,PoR,PoL,U1R,U1L,U1RA,U1LA,U6R,U6L,L1R,L1AR,A_point,B_point,POG = input_file(file)
    
    msgbox.showwarning(title="경고!",message="데이터를 입력하였다면, FH plane과 sp plane을 먼저 실행해주세요.")
    
def delete():
            ax.clear()
            label_fh.destroy
            plot_cube(ax)
            canvas.draw()
#---------------radio button의 event함수들 정의---------------
#평면 구해서 canvas에 그리기
def fh_plane_event():
    global fh_plane
    solve_FH_Plane.plot()

def op_plane_event():
    global op_plane
    OP_plane = two_point_middle_point_plane(canvas=canvas,ax=ax,root=root,
                                        point1=U6L,point2=U6R,middle_point1=U1R,middle_point2=U1L,
                                        label='OP plane',color='green')
    op_plane = OP_plane.plane()
    OP_plane.plot()
def sp_plane_event():
    global sp_plane
    solve_SP_plane = SP_Plane(canvas=canvas,ax=ax,root=root,
                          n_point=N_point, s_point=S_point,FH_plane=fh_plane,
                          label='SP plane', color='skyblue')
    sp_plane = solve_SP_plane.plane()
    solve_SP_plane.plot()
def XZ_plane_event():
    solve_XZ_plane = XZ_Plane(canvas=canvas, ax=ax,root=root,
                          FH_plane=fh_plane,n_point=N_point,
                          label='XZ plane', color='violet')
    solve_XZ_plane.plot()
def xy_plane_event():
    global coronal_plane
    solve_xy_plane = XY_Plane(canvas=canvas, ax=ax, root=root,
                          FH_plane=fh_plane, SP_plane=sp_plane,n_point=N_point,
                          label='xy plane', color='yellowgreen')
    coronal_plane = solve_xy_plane.plane()
    solve_xy_plane.plot()

#angle값 밑에 찍어주고, canvas에 도형 그리기
def sna_event():
    sna = Three_point_angle(canvas=canvas, ax=ax, root=root,
                    point1=S_point, point2=N_point, point3=A_point,
                    label='SNA')
    sna.draw_event()
def snb_event():
    snb = Three_point_angle(canvas=canvas, ax=ax, root=root,
                        point1=S_point, point2=N_point, point3=B_point,
                        label='SNB')
    snb.draw_event()
def anb_event():
    anb = Three_point_angle(canvas=canvas, ax=ax, root=root,
                        point1=A_point, point2=N_point, point3=B_point,
                        label='ANB')
    anb.draw_event()
def u1_sn_event():
    solve_sn_plane = SP_Plane(canvas=canvas,ax=ax,root=root,
                    n_point=N_point,s_point=S_point,FH_plane=sp_plane,
                    label="SN plane",color='purple') #U1-SN에 필요한 Sn plane 구하기
    sn_plane = solve_sn_plane.plane()
    u1sn = Point_and_plane_angle(canvas=canvas,ax=ax,root=root,
                                point1=U1R,point2=U1RA,plane=sn_plane,label='U1-SN')
    u1sn.draw_event()
def op_fh_angle_event():
    op_fh_angle = Two_Plane_Angle(canvas=canvas, ax=ax, root=root,
                              plane1=op_plane,plane2=fh_plane,label='OP-FH')
    op_fh_angle.draw_event()
    
#distance 밑에 찍어주고, canvas에 도형 그리기
def overjet_event():
    overjet = Two_point_distance(root=root, canvas=canvas,ax=ax,
                             point1=U1R,point2=L1R,label="overjet")
    overjet.draw_event()
def overbite_event():
    overbite = Two_point_distance(root=root, canvas=canvas,ax=ax,
                             point1=U1R,point2=L1R,label="overbite")
    overbite.draw_event()
def u1z_event():
    u1z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=U1R,plane=coronal_plane,label='U1-Z')
    u1z.draw_event()
def a_z_event():
    a_z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=A_point,plane=coronal_plane,label='A-Z')
    a_z.draw_event()
def pog_z_event():
    pog_z = Point_and_Plane_distance(root=root,canvas=canvas,ax=ax,
                               point=POG,plane=coronal_plane,label='Pog-Z')
    pog_z.draw_event()
#---------------3d cube 그리기---------------
fig = plt.Figure(figsize=(5, 5), tight_layout=True) #3d cube 그릴 캔버스 생성
ax = fig.add_subplot(111, projection='3d') #canvas 3D로 변경
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) #캔버스 화면 좌측에 고정시키기
plot_cube(ax) #cube 그리기

#---------------파일 받거나 plot 삭제할 button 만들기---------------
input_button = tk.Button(root, text="txt파일 받아오기",command=input_file_event)
input_label = tk.Label(root,text="파일은 오스템 데이터 기준으로 읽어냅니다")
input_label2 = tk.Label(root, text="혹시 다른 데이터를 넣고 싶다면, 오스템 data format으로 변경해주셔야 합니다.")
input_button.pack(side=tk.TOP)
input_label.pack()
input_label2.pack()

delete_button = tk.Button(root, text="plot reset",command=delete,height=5,width=10,bg='red',fg='white')
delete_button.pack(side=tk.BOTTOM,pady=10)

#---------------해당 연산과 관련된 radio button 보여줄checkbutton---------------
plane_ckbutton = tk.Checkbutton(root, text="평면 구하기",command=plane_cb_event)
plane_ckbutton.pack()
angle_ckbutton = tk.Checkbutton(root, text="각도 구하기",command=angle_ck_event)
angle_ckbutton.pack()
distance_ckbutton = tk.Checkbutton(root, text="거리 구하기",command=distnace_ck_event)
distance_ckbutton.pack()

#---------------평면 구하기---------------
plane_value = tk.IntVar()

FH_Plane_button = tk.Radiobutton(root,text="FH 평면 구하기",value=1,command=fh_plane_event,variable=plane_value)
solve_FH_Plane = two_point_middle_point_plane(canvas=canvas, ax=ax, root=root,
                                        point1=OrR,point2=OrL,middle_point1=PoR, middle_point2=PoL,
                                        label='FH plane',color="None")
fh_plane = solve_FH_Plane.plane()
label_fh = draw_plane(root=root,ax=ax,plane=fh_plane,
                           label=f'FH plane', color='yellow')
label_fh.pack()
FH_Plane_button.pack_forget()

OP_Plane_button = tk.Radiobutton(root, text='OP 평면 구하기',value=2,command=op_plane_event,variable=plane_value)
OP_Plane_button.pack_forget()

SP_plane_button = tk.Radiobutton(root, text='SP 평면 구하기',value=3,command=sp_plane_event,variable=plane_value)
SP_plane_button.pack_forget()

XZ_plane_button = tk.Radiobutton (root, text='XZ 평면 구하기',value=4,command=XZ_plane_event,variable=plane_value)
XZ_plane_button.pack_forget()

XY_plane_button = tk.Radiobutton(root, text='XY 평면 구하기',value=5,command=xy_plane_event,variable=plane_value)
XY_plane_button.pack_forget()

#---------------각도 구하기---------------
angle_value = tk.IntVar()
three_point_angle1 = tk.Radiobutton(root,text="SNA", value=1, command=sna_event,variable=angle_value)
three_point_angle1.pack_forget()

three_point_angle2 = tk.Radiobutton(root,text="SNB", value=2, command=snb_event,variable=angle_value)
three_point_angle2.pack_forget()

three_point_angle3 = tk.Radiobutton(root,text="ANB", value=3, command=anb_event,variable=angle_value)
three_point_angle3.pack_forget()

point_and_plane_angle1 = tk.Radiobutton(root,text="U1-SN", value=4, command=u1_sn_event,variable=angle_value)
point_and_plane_angle1.pack_forget()
# lmpa = Point_and_plane_angle(canvas=canvas,ax=ax,root=root,
#                              point1=L1R,point2=U1RA,plane=sn_plane,label='1MPA')
# point_and_plane_angle2 = tk.Radiobutton(root,text="1MPA", value=5, command=None,variable=angle_value)
# point_and_plane_angle2.pack()

plane_and_plane_angle = tk.Radiobutton(root,text="OP-FH", value=6, command=op_fh_angle_event,variable=angle_value)
plane_and_plane_angle.pack_forget()

#---------------거리 구하기---------------
point_distance1 = tk.Radiobutton(root,text="Overjet", value=7, command=overjet_event,variable=angle_value)
point_distance1.pack_forget()

point_distance2 = tk.Radiobutton(root,text="Overbite", value=8, command=overbite_event,variable=angle_value)
point_distance2.pack_forget()

point_and_plane_distance1 = tk.Radiobutton(root,text="U1-Z", value=9, command=u1z_event,variable=angle_value)
point_and_plane_distance1.pack_forget()

point_and_plane_distance2 = tk.Radiobutton(root,text="A-Z", value=10, command=a_z_event,variable=angle_value)
point_and_plane_distance2.pack_forget()

point_and_plane_distance3 = tk.Radiobutton(root,text="Pog-Z", value=11, command=pog_z_event,variable=angle_value)
point_and_plane_distance3.pack_forget()

root.mainloop()