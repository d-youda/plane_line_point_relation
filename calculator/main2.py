import tkinter as Tk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import plot_cube
from radio_button_class import two_point_middle_point_plane,SP_Plane,XZ_plane,XY_plane
import numpy as np

#---------------input 점들 값 받기---------------
N_point = np.array([99.49, 50.13, 144.23])
S_point = np.array([94.48, 114.44, 137.32])
OrR = np.array([64.97, 55.87, 117.8])
OrL = np.array([130.82, 62.57, 112.91])
PoR = np.array([24.49, 131.81, 120.23])
PoL = np.array([154.21, 144.01, 110.83])
U1R = np.array([91.13, 45.32, 59.54])
U1L = np.array([99.86, 46.19, 59.61])
U6R = np.array([65.31, 71.83, 67.11])
U6L = np.array([121.69, 76.23, 62.55])
root = tk.Tk() #tk 객체 생성

#---------------checkbutton의 event함수들 정의---------------
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
#---------------3d cube 그리기---------------
fig = plt.Figure(figsize=(5, 5), tight_layout=True) #3d cube 그릴 캔버스 생성
ax = fig.add_subplot(111, projection='3d') #canvas 3D로 변경
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) #캔버스 화면 좌측에 고정시키기
plot_cube(ax) #cube 그리기

#---------------평면 구하기---------------
solve_FH_Plane = two_point_middle_point_plane(canvas=canvas, ax=ax, root=root,
                                        point1=OrR,point2=OrL,middle_point1=PoR, middle_point2=PoL,
                                        label='FH plane',color='yellow')
FH_plane = solve_FH_Plane.plane()
FH_Plane_button = tk.Radiobutton(root,text="FH 평면 구하기",command=fh_plane_event)
FH_Plane_button.pack()

OP_plane = two_point_middle_point_plane(canvas=canvas,ax=ax,root=root,
                                        point1=U6L,point2=U6R,middle_point1=U1R,middle_point2=U1L,
                                        label='OP plane',color='green')
OP_Plane_button = tk.Radiobutton(root, text='OP 평면 구하기',command=op_plane_event)
OP_Plane_button.pack()

solve_SP_plane = SP_Plane(canvas=canvas,ax=ax,root=root,
                          n_point=N_point, s_point=S_point,FH_plane=FH_plane,
                          label='SP plane', color='blue')
sp_plane = solve_SP_plane.plane()
SP_plane_button = tk.Radiobutton(root, text='SP 평면 구하기',command=sp_plane_event)
SP_plane_button.pack()

solve_XZ_plane = XZ_plane(canvas=canvas, ax=ax,root=root,
                          FH_plane=FH_plane,n_point=N_point,
                          label='XZ plane', color='violet')
XZ_plane_button = tk.Radiobutton(root, text='XZ 평면 구하기',command=XZ_plane_event)
XZ_plane_button.pack()

solve_xy_plane = XY_plane(canvas=canvas, ax=ax, root=root,
                          FH_plane=FH_plane, SP_plane=sp_plane,n_point=N_point,
                          label='xy plane', color='orange')
XY_plane_button = tk.Radiobutton(root, text='XY 평면 구하기',command=xy_plane_event)
XY_plane_button.pack()
root.mainloop()