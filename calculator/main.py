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
from button import draw_plane,draw_point,draw_line
from math_method.point import middle_two_point

#-----체크 박스 선택 or 해제 알기 위한 global 변수-------
plane = 0
angle = 0
distance = 0

class App():
    def __init__(self, root):
        self.root = root
        self.plane = 0
        self.angle = 0
        self.distance = 0

        self.n_point = np.array([0,0,0])
        self.s_point = np.array([0,0,0])
        self.OrR = np.array([0,0,0])
        self.OrL = np.array([0,0,0])
        self.PoR = np.array([0,0,0])
        self.PoL = np.array([0,0,0])
        self.u1R = np.array([0,0,0])
        self.u1L = np.array([0,0,0])
        self.u1RA = np.array([0,0,0])
        self.u1LA=np.array([0,0,0])
        self.u6R=np.array([0,0,0])
        self.u6L=np.array([0,0,0])
        self.L1R=np.array([0,0,0])
        self.L1AR=np.array([0,0,0])
        self.a_point=np.array([0,0,0])
        self.b_point=np.array([0,0,0])
        self.pog = np.array([0,0,0])

        self.XY_plane = np.array([0,0,0,0])
        self.XZ_plane = np.array([0,0,0,0])
        self.SP_plane = np.array([0,0,0,0])
        self.FH_plane = np.array([0,0,0,0])
        self.OP_plane = np.array([0,0,0,0])
        self.SN_plane = np.array([0,0,0,0])
        self.fH_label = tk.Label()
        self.op_label = tk.Label()
        self.sp_label = tk.Label()
        self.xz_label=tk.Label()
        self.xy_label =tk.Label()
        self.SNA_label = tk.Label()
        self.SNB_label = tk.Label()
        self.ANB_label = tk.Label()
        self.U1SN_label = tk.Label()
        self.OPFH_label = tk.Label()
        self.overjet_label = tk.Label()
        self.overbite_label = tk.Label()
        self.u1z_label = tk.Label()
        self.a_z_label = tk.Label()
        self.pogz_label = tk.Label()

        #캔버스 생성
        fig = plt.Figure(figsize=(5, 5), tight_layout=True) #3d cube 그릴 캔버스 생성
        self.ax = fig.add_subplot(111, projection='3d') #canvas 3D로 변경
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) #캔버스 화면 좌측에 고정시키기
        plot_cube(self.ax) #cube 그리기

        #버튼 삽입
        self.input_button = tk.Button(self.root, text="txt파일 받아오기", command=self.input_file_event)
        self.input_label = tk.Label(root,text="파일은 오스템 데이터 기준으로 읽어냅니다")
        self.input_label2 = tk.Label(root, text="혹시 다른 데이터를 넣고 싶다면, 오스템 data format으로 변경해주셔야 합니다.")
        self.input_button.pack(side=tk.TOP)
        self.input_label.pack()
        self.input_label2.pack()

        self.delete_button = tk.Button(root, text="plot reset",command=self.delete,height=5,width=10,bg='red',fg='white')
        self.delete_button.pack(side=tk.BOTTOM,pady=10)

        #checkbox 삽입
        self.plane_ckbutton = tk.Checkbutton(root, text="평면 구하기",command=self.plane_cb_event)
        self.plane_ckbutton.pack()
        self.angle_ckbutton = tk.Checkbutton(root, text="각도 구하기",command=self.angle_cb_event)
        self.angle_ckbutton.pack()
        self.distance_ckbutton = tk.Checkbutton(root, text="거리 구하기",command=self.distnace_cb_event)
        self.distance_ckbutton.pack()

        #plane radion button(check box 선택하면 나오도록 하기 위해 forget해두기)
        plane_value = tk.IntVar()
        self.fh_plane_rb = tk.Radiobutton(root,text="FH 평면 구하기",value=1,command=self.fh_plane_event,variable=plane_value)
        self.fh_plane_rb.pack_forget()
        self.op_plane_rb = tk.Radiobutton(root, text='OP 평면 구하기',value=2,command=self.op_plane_event,variable=plane_value)
        self.op_plane_rb.pack_forget() 
        self.sp_plane_rb = tk.Radiobutton(root, text='SP 평면 구하기',value=3,command=self.sp_plane_event,variable=plane_value)
        self.sp_plane_rb.pack_forget()
        self.xz_plane_rb = tk.Radiobutton (root, text='XZ 평면 구하기',value=4,command=self.xz_plane_event,variable=plane_value)
        self.xz_plane_rb.pack_forget()
        self.xy_plane_rb = tk.Radiobutton(root, text='XY 평면 구하기',value=5,command=self.xy_plane_event,variable=plane_value)
        self.xy_plane_rb.pack_forget()

        #angle radio button(check box 선택하면 나오도록 하기 위해 forget해두기)
        angle_value = tk.IntVar()
        self.sna_rb = tk.Radiobutton(root,text="SNA", value=1, command=self.sna_event,variable=angle_value)
        self.sna_rb.pack_forget()
        self.snb_rb = tk.Radiobutton(root,text="SNB", value=2, command=self.snb_event,variable=angle_value)
        self.snb_rb.pack_forget()
        self.anb_rb = tk.Radiobutton(root,text="ANB", value=3, command=self.anb_event,variable=angle_value)
        self.anb_rb.pack_forget()
        self.u1sn_rb = tk.Radiobutton(root,text="U1-SN", value=4, command=self.u1_sn_event,variable=angle_value)
        self.u1sn_rb.pack_forget()
        self.opfh_rb = tk.Radiobutton(root,text="OP-FH", value=5, command=self.op_fh_angle_event,variable=angle_value)
        self.opfh_rb.pack_forget()
        
        #distance radio button(check box 선택하면 나오도록 하기 위해 forget해두기)
        distance_value = tk.IntVar()
        self.overjet_rb = tk.Radiobutton(root,text="Overjet", value=1, command=self.overjet_event,variable=distance_value)
        self.overjet_rb.pack_forget()
        self.overbite_rb = tk.Radiobutton(root,text="Overbite", value=2, command=self.overbite_event,variable=distance_value)
        self.overbite_rb.pack_forget()
        self.u1z_rb = tk.Radiobutton(root,text="U1-Z", value=3, command=self.u1z_event,variable=distance_value)
        self.u1z_rb.pack_forget()
        self.az_rb = tk.Radiobutton(root,text="A-Z", value=4, command=self.a_z_event,variable=distance_value)
        self.az_rb.pack_forget()
        self.pog_z_rb = tk.Radiobutton(root,text="Pog-Z", value=5, command=self.pog_z_event,variable=distance_value)
        self.pog_z_rb.pack_forget()


    def find_the_plane(self):
        '''기준 평면 구하는 함수'''
        op_plane = two_point_middle_point_plane(canvas=self.canvas,ax=self.ax,root=self.root,
                                        point1=self.u6L,point2=self.u6R,middle_point1=self.u1R,middle_point2=self.u1L,
                                        label='OP plane',color='green')
        self.OP_plane = op_plane.plane() #평면 결정

        fh_plane = two_point_middle_point_plane(canvas=self.canvas, ax=self.ax, root=self.root,
                                        point1=self.OrR,point2=self.OrL,middle_point1=self.PoR, middle_point2=self.PoL,
                                        label='FH plane',color="None")
        self.FH_plane = fh_plane.plane()

        sp_plane = SP_Plane(canvas=self.canvas,ax=self.ax,root=self.root,
                          n_point=self.n_point, s_point=self.s_point,FH_plane=self.FH_plane,
                          label='SP plane', color='skyblue')
        self.SP_plane = sp_plane.plane() #평면 결정

        xz_plane = XZ_Plane(canvas=self.canvas, ax=self.ax,root=self.root,FH_plane=self.FH_plane,n_point=self.n_point, label='XZ plane', color='violet')
        self.XZ_plane = xz_plane.plane()

        xy_plane = XY_Plane(canvas=self.canvas, ax=self.ax, root=self.root,
                          FH_plane=self.FH_plane, SP_plane=self.SP_plane ,n_point=self.n_point,
                          label='xy plane', color='yellowgreen')
        self.XY_plane = xy_plane.plane()

    

    def input_file_event(self):
        file = filedialog.askopenfilename()
        self.n_point,self.s_point,self.OrR,self.OrL,self.PoR,self.PoL,self.u1R,self.u1L,self.u1RA,self.u1LA,self.u6R,self.u6L,self.L1R,self.L1AR,self.a_point,self.b_point,self.pog = input_file(file)
        # 파일에서 불러오자마자 평면 구해서 저장해두기
        self.find_the_plane()

    def plane_cb_event(self):
        global plane
        '''plane을 구하는 checkbutton 눌렀을 때 실행시킬 이벤트함수'''
        if plane==0:
            self.fh_plane_rb.pack()
            self.op_plane_rb.pack()
            self.sp_plane_rb.pack()
            self.xz_plane_rb.pack()
            self.xy_plane_rb.pack()
            plane += 1

        elif plane==1:
            self.fh_plane_rb.pack_forget()
            self.op_plane_rb.pack_forget()
            self.sp_plane_rb.pack_forget()
            self.xz_plane_rb.pack_forget()
            self.xy_plane_rb.pack_forget()

            plane = 0

    def angle_cb_event(self):
        global angle
        '''각도 구하는 checkbutton 눌렀을 때 실행시키는 이벤트함수'''
        if angle==0:
            self.sna_rb.pack()
            self.snb_rb.pack()
            self.anb_rb.pack()
            self.u1sn_rb.pack()
            self.opfh_rb.pack()
            angle += 1
        elif angle==1:
            self.sna_rb.pack_forget()
            self.snb_rb.pack_forget()
            self.anb_rb.pack_forget()
            self.u1sn_rb.pack_forget()
            self.opfh_rb.pack_forget()
            angle = 0

    def distnace_cb_event(self):
        global distance
        '''거리 구하는 checkbutton 눌렀을 때 실행시키는 이벤트함수'''
        if distance==0:
            self.overjet_rb.pack()
            self.overbite_rb.pack()
            self.u1z_rb.pack()
            self.az_rb.pack()
            self.pog_z_rb.pack()
            distance += 1
        elif distance==1:
            self.overjet_rb.pack_forget()
            self.overbite_rb.pack_forget()
            self.u1z_rb.pack_forget()
            self.az_rb.pack_forget()
            self.pog_z_rb.pack_forget()
            distance=0

    def fh_plane_event(self):
        '''fh plane 라디오 버튼 클릭하면 화면에 plane 그리고, label 출력하기'''
        self.fH_label= draw_plane(root=self.root, ax=self.ax, plane=self.FH_plane,label='FH plane',
                   color='green')
        self.fH_label.pack()
        draw_point(self.ax,point=self.u6L)
        draw_point(self.ax,point=self.u6R)
        middle_point = middle_two_point(point1=self.PoR, point2=self.PoL)
        draw_point(self.ax,point=middle_point)
        self.canvas.draw()

    def op_plane_event(self):
        '''op plane 라디오 버튼 클릭하면 화면에 plane 그리고, label 출력하기'''
        self.op_label = draw_plane(root=self.root,ax=self.ax,plane=self.OP_plane, label=f'OP plane')
        self.op_label.pack()
        draw_point(self.ax,point=self.u6L)
        draw_point(self.ax,point=self.u6R)
        middle_point = middle_two_point(point1=self.u1R, point2=self.u1L) 
        draw_point(self.ax,point=middle_point)
        self.canvas.draw()

    def sp_plane_event(self):
        '''sp plane 라디오 버튼 클릭하면 화면에 plane 그리고, label 출력하기'''
        self.sp_label = draw_plane(root=self.root,ax=self.ax,plane=self.SP_plane,
                           label=f'SP plane', color='skyblue')
        self.sp_label.pack()
        draw_point(ax=self.ax, point=self.n_point)
        draw_point(ax=self.ax, point=self.s_point)
        self.canvas.draw()
    
    def xz_plane_event(self):
        '''xz plane 라디오 버튼 클릭하면 화면에 plane 그리고, label 출력하기'''
        self.xz_label = draw_plane(root=self.root,ax=self.ax,plane=self.XZ_plane,
                           label=f'XZ plane', color='violet')
        self.xz_label.pack()
        draw_point(ax=self.ax, point=self.n_point)
        self.canvas.draw()

    def xy_plane_event(self):
        '''xy plane 라디오 버튼 클릭하면 화면에 plane 그리고, label 출력하기'''
        self.xy_label = draw_plane(root=self.root,ax=self.ax,plane=self.XY_plane,
                           label=f'XY plane', color='yellowgreen')
        self.xy_label.pack()
        draw_point(ax=self.ax, point=self.n_point)
        self.canvas.draw()

    #angle radio event function
    def sna_event(self):
        '''sna 라디오 버튼 클릭하면 sna 값 구하고, 점 찍기'''
        SNA = Three_point_angle(canvas=self.canvas, ax=self.ax, root=self.root,
                                 point1=self.s_point, point2=self.n_point, point3=self.a_point,
                                 label="SNA")
        self.SNA_label = tk.Label(self.root, text=f"SNA 각도:{SNA.angle()}")
        self.SNA_label.pack()
        draw_point(ax=self.ax,point=self.s_point,color='red')
        draw_point(ax=self.ax,point=self.n_point,color='green')
        draw_point(ax=self.ax,point=self.a_point,color='blue')
        self.canvas.draw()
    
    def snb_event(self):
        SNB = Three_point_angle(canvas=self.canvas, ax=self.ax, root=self.root,
                                 point1=self.s_point, point2=self.n_point, point3=self.b_point,
                                 label="SNA")
        self.SNB_label = tk.Label(self.root, text=f"SNA 각도:{SNB.angle()}")
        self.SNB_label.pack()
        draw_point(ax=self.ax,point=self.s_point,color='red')
        draw_point(ax=self.ax,point=self.n_point,color='green')
        draw_point(ax=self.ax,point=self.b_point,color='blue')
        self.canvas.draw()

    def anb_event(self):
        ANB = Three_point_angle(canvas=self.canvas, ax=self.ax, root=self.root,
                                 point1=self.a_point, point2=self.n_point, point3=self.b_point,
                                 label="SNA")
        self.ANB_label = tk.Label(self.root, text=f"SNA 각도:{ANB.angle()}")
        self.ANB_label.pack()
        draw_point(ax=self.ax,point=self.a_point,color='red')
        draw_point(ax=self.ax,point=self.n_point,color='green')
        draw_point(ax=self.ax,point=self.b_point,color='blue')
        self.canvas.draw()
        
    def u1_sn_event(self):
        sn_plane = SP_Plane(canvas=self.canvas, ax=self.ax, root=self.root,
                    n_point=self.n_point,s_point=self.s_point,FH_plane=self.SP_plane,
                    label="SN plane",color='purple') #U1-SN에 필요한 Sn plane 구하기
        self.SN_plane=sn_plane.plane()
        U1SN = Point_and_plane_angle(canvas=self.canvas, ax=self.ax, root=self.root,
                                point1=self.u1R,point2=self.u1RA,plane=self.SN_plane,label='U1-SN')
        self.U1SN_label = tk.Label(self.root, text=f"U1SN 각도:{U1SN.angle()}")
        self.U1SN_label.pack()
        draw_point(ax=self.ax,point=self.u1R,color='red')
        draw_point(ax=self.ax,point=self.u1RA,color='blue')
        draw_line(ax=self.ax, point1=self.u1R,point2=self.u1RA)
        draw_plane(root=self.root, ax=self.ax,plane=self.SN_plane,label='SN plane')
        self.canvas.draw()

    def op_fh_angle_event(self):
        OP_FH = Two_Plane_Angle(canvas=self.canvas, ax=self.ax, root=self.root,
                              plane1=self.OP_plane,plane2=self.FH_plane,label='OP-FH')
        self.OPFH_label =  tk.Label(self.root, text=f"OP_FH 각도:{OP_FH.angle()}")
        self.OPFH_label.pack()
        draw_plane(root=self.root,ax=self.ax,plane=self.OP_plane,label='OP plane')
        draw_plane(root=self.root,ax=self.ax,plane=self.FH_plane,label='OP plane',color='yellow')
        self.canvas.draw()

    def overjet_event(self):
        overjet = Two_point_distance(root=self.root, canvas=self.canvas,ax=self.ax,
                             point1=self.u1R,point2=self.L1R,label="overjet")
        self.overjet_label = tk.Label(self.root, text=f"overjet 거리: {overjet.distance()}")
        self.overjet_label.pack()
        draw_point(ax=self.ax, point=self.L1R)
        draw_point(ax=self.ax, point=self.u1R, color='green')
        self.canvas.draw()
         
    def overbite_event(self):
        overbite = Two_point_distance(root=self.root, canvas=self.canvas,ax=self.ax,
                             point1=self.u1R,point2=self.L1R,label="overbite")
        self.overbite_label = tk.Label(self.root, text=f"overbite 거리: {overbite.distance()}")
        self.overbite_label.pack()
        draw_point(ax=self.ax, point=self.L1R)
        draw_point(ax=self.ax, point=self.u1R, color='green')
        self.canvas.draw()

    def u1z_event(self):
        u1z = Point_and_Plane_distance(root=self.root, canvas=self.canvas,ax=self.ax,
                               point=self.u1R,plane=self.XY_plane,label='U1-Z')
        self.u1z_label = tk.Label(self.root, text=f"u1z 거리: {u1z.distance()}")
        self.u1z_label.pack()
        draw_point(ax=self.ax, point=self.u1R)
        draw_plane(root=self.root, ax=self.ax, plane=self.XY_plane,label='Coronal')
        self.canvas.draw()

    def a_z_event(self):
        a_z = Point_and_Plane_distance(root=self.root, canvas=self.canvas,ax=self.ax,
                               point=self.a_point,plane=self.XY_plane,label='A-Z')
        self.a_z_label = tk.Label(self.root, text=f"u1z 거리: {a_z.distance()}")
        self.a_z_label.pack()
        draw_point(ax=self.ax, point=self.u1R)
        draw_plane(root=self.root, ax=self.ax, plane=self.XY_plane,label='Coronal')
        self.canvas.draw()

    def pog_z_event(self):
        pogz = Point_and_Plane_distance(root=self.root, canvas=self.canvas,ax=self.ax,
                               point=self.a_point,plane=self.XY_plane,label='POG-Z')
        self.pogz_label = tk.Label(self.root, text=f"u1z 거리: {pogz.distance()}")
        self.pogz_label.pack()
        draw_point(ax=self.ax, point=self.a_point)
        draw_plane(root=self.root, ax=self.ax, plane=self.XY_plane,label='Coronal')
        self.canvas.draw()

    def delete(self):
        self.ax.clear()
        plot_cube(self.ax)
        self.canvas.draw()
        #delete 누르면 label들도 다 삭제
        self.fH_label.after(1,self.fH_label.destroy())
        self.op_label.after(1,self.op_label.destroy())
        self.sp_label.after(1,self.sp_label.destroy())
        self.xz_label.after(1,self.xz_label.destroy())
        self.xy_label.after(1,self.xy_label.destroy())
        self.SNA_label.after(1,self.SNA_label.destroy())
        self.SNB_label.after(1,self.SNB_label.destroy())
        self.ANB_label.after(1,self.ANB_label.destroy())
        self.U1SN_label.after(1,self.U1SN_label.destroy())
        self.OPFH_label.after(1,self.OPFH_label.destroy())
        self.overjet_label.after(1,self.overjet_label.destroy())
        self.overbite_label.after(1,self.overbite_label.destroy())
        self.u1z_label.after(1,self.u1z_label.destroy())
        self.a_z_label.after(1,self.a_z_label.destroy())
        self.pogz_label.after(1,self.pogz_label.destroy())
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()