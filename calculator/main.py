import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import plot_cube
from action_function import point_make_plane,make_fh_plane,make_sp_plane,make_xz_plane,make_xy_plane,slove_three_point_angle,solve_plane_and_line_angle,solve_plane_and_line_angle2,solve_two_plane_angle,solve_two_point_distance,solve_point_and_plane_distance
op = 0
mp = 0
fh = 0
sp = 0
xz = 0
xy = 0

three_point = 0
plane_line = 0
plane_line2 = 0
opandfh = 0
two_point = 0
point_plane = 0
def main():
    def delete():
            ax.clear()
            plot_cube(ax)
            canvas.draw()
    def OP_plane_event():
        global op
        if op==0:
            label.pack()
            entry_point1.pack()
            entry_point2.pack()
            entry_point3.pack()
            button_add_point.pack()
            op+=1

        elif op==1:
            label.pack_forget()
            entry_point1.pack_forget()
            entry_point2.pack_forget()
            entry_point3.pack_forget()
            button_add_point.pack_forget()
            op=0

    def OP_plane():
        point_make_plane(root=app, ax=ax, canvas=canvas,
                            entry_point1=entry_point1,entry_point2=entry_point2,entry_point3=entry_point3,
                            plane_name='OP 평면')
    def MP_plane_event():
        global mp
        if mp==0:
            label2.pack()
            entry2_point1.pack()
            entry2_point2.pack()
            entry2_point3.pack()
            button_add_point2.pack()            
            mp+=1

        elif mp==1:
            label2.pack_forget()
            entry2_point1.pack_forget()
            entry2_point2.pack_forget()
            entry2_point3.pack_forget()
            button_add_point2.pack_forget()
            mp=0

    def MP_plane():
        point_make_plane(root=app, ax=ax, canvas=canvas,
                            entry_point1=entry2_point1,entry_point2=entry2_point2,entry_point3=entry2_point3,
                            plane_name="MP 평면")     
    def FH_plane_event():
        global fh
        if fh==0:
            fh_label1.pack()
            fh_entry1.pack()
            fh_entry2.pack()
            fh_entry3.pack()
            fh_entry4.pack()
            button_add_point3.pack()          
            fh+=1

        elif fh==1:
            fh_label1.pack_forget()
            fh_entry1.pack_forget()
            fh_entry2.pack_forget()
            fh_entry3.pack_forget()
            fh_entry4.pack_forget()
            button_add_point3.pack_forget()
            fh=0

    def FH_plane():
        make_fh_plane(app,ax,canvas,fh_entry1,fh_entry2,fh_entry3,fh_entry4,plane_name = 'FH 평면')

    def SP_plane_event():
        global sp
        if sp==0:
            sp_label.pack()
            sp_n_label.pack()
            sp_n_entry.pack()
            sp_s_label.pack()
            sp_s_entry.pack()
            sp_plane_label.pack()
            sp_plane_entry.pack()
            button_add_point4.pack()
            sp += 1
        elif sp==1:
            sp_label.pack_forget()
            sp_n_label.pack_forget()
            sp_n_entry.pack_forget()
            sp_s_label.pack_forget()
            sp_s_entry.pack_forget()
            sp_plane_label.pack_forget()
            sp_plane_entry.pack_forget()
            button_add_point4.pack_forget()
            sp = 0

    def SP_plane():
        make_sp_plane(app,ax,canvas,sp_n_entry,sp_s_entry,sp_plane_entry,plane_name = 'SP 평면')
    
    def XZ_plane_event():
        global xz
        if xz==0:
            xz_label.pack()
            plane_label.pack()
            fh_plane_entry.pack()
            xz_n_point_label.pack()
            xz_n_point_entry.pack()
            button_add_point5.pack()
            xz += 1

        elif xz==1:
            xz_label.pack_forget()
            plane_label.pack_forget()
            fh_plane_entry.pack_forget()
            xz_n_point_label.pack_forget()
            xz_n_point_entry.pack_forget()
            button_add_point5.pack_forget()
            xz=0

    def XZ_plane():
        make_xz_plane(app,ax,canvas,fh_plane_entry,xz_n_point_entry)

    def XY_plane_event():
        global xy
        if xy==0:
            xy_label.pack()
            xy_point_label.pack()
            xy_point_entry.pack()
            xy_fh_plane.pack()
            xy_sp_plane.pack()
            button_add_point6.pack()
            xy +=1
        elif xy==1:
            xy_label.pack_forget()
            xy_point_label.pack_forget()
            xy_point_entry.pack_forget()
            xy_fh_plane.pack_forget()
            xy_sp_plane.pack_forget()
            button_add_point6.pack_forget()
            xy=0
    def XY_plane():
        make_xy_plane(app,ax,canvas,xy_fh_plane,xy_sp_plane,xy_point_entry)
    
    def threee_point_angle_event():
        global three_point
        if three_point==0:
            point_label.pack()
            point1_entry.pack()
            point2_entry.pack()
            point3_entry.pack()
            button_add_point7.pack()
            three_point += 1
        elif three_point==1:
            point_label.pack_forget()
            point1_entry.pack_forget()
            point2_entry.pack_forget()
            point3_entry.pack_forget()
            button_add_point7.pack_forget()
            three_point = 0
    def three_point_angle():
        slove_three_point_angle(app,ax,canvas,point1_entry,point2_entry,point3_entry)
    def plane_line_angle_envet():
        global plane_line
        if plane_line==0:
            line_label.pack()
            u1_point_entry.pack()
            u1a_point_entry.pack()
            plane_point.pack()
            s_point_entry.pack()
            n_point_entry.pack()
            sp_plane_label2.pack()
            sp_plane_entry2.pack()
            button_add_point7.pack()
            plane_line += 1
        elif plane_line==1:
            line_label.pack_forget()
            u1_point_entry.pack_forget()
            u1a_point_entry.pack_forget()
            plane_point.pack_forget()
            s_point_entry.pack_forget()
            n_point_entry.pack_forget()
            sp_plane_label2.pack_forget()
            sp_plane_entry2.pack_forget()
            button_add_point7.pack_forget()
            plane_line = 0
    def plane_line_angle():
        solve_plane_and_line_angle(app,ax,canvas,u1_point_entry,u1a_point_entry,s_point_entry,n_point_entry,sp_plane_entry2,plane_name="SP 평면")

    def plane_line_angle_envet2():
        global plane_line2
        if plane_line2==0:
            button9_label.pack()
            l1.pack()
            l1a.pack()
            button9_label2.pack()
            mp_plane.pack()
            button_add_point9.pack()
            plane_line2 += 1

        elif plane_line2==1:
            button9_label.pack_forget()
            l1.pack_forget()
            l1a.pack_forget()
            button9_label2.pack_forget()
            mp_plane.pack_forget()
            button_add_point9.pack_forget()
            plane_line2 =0
    def plane_line_angle2():
        solve_plane_and_line_angle2(app,ax,canvas,l1,l1a,mp_plane)
    
    def OP_and_FH_event():
        global opandfh
        if opandfh==0:
            button10_label.pack()
            op_plane.pack()
            fh_plane.pack()
            button_add_point10.pack()
            opandfh += 1
        elif opandfh==1:
            button10_label.pack_forget()
            op_plane.pack_forget()
            fh_plane.pack_forget()
            button_add_point10.pack_forget()
            opandfh =0
    def OP_FH_angle():
        solve_two_plane_angle(app,ax,canvas,op_plane,fh_plane)

    def two_point_distance_event():
        global two_point
        if two_point==0:
            button11_label.pack()
            button11_point1.pack()
            button11_point2.pack()
            button_add_point11.pack()
            two_point += 1
        elif two_point==1:
            button11_label.pack_forget()
            button11_point1.pack_forget()
            button11_point2.pack_forget()
            button_add_point11.pack_forget()
            two_point=0
    def two_point_distance():
        solve_two_point_distance(app,ax,canvas,button11_point1,button11_point2)

    def point_plane_distance_event():
        global point_plane
        if point_plane==0:
            button12_label.pack()
            button12_point.pack()
            button12_plane.pack()
            button_add_point12.pack()
            point_plane += 1
        elif point_plane==1:
            button12_label.pack_forget()
            button12_point.pack_forget()
            button12_plane.pack_forget()
            button_add_point12.pack_forget()
            point_plane = 0
    def point_plane_distance():
        solve_point_and_plane_distance(app,ax,canvas,button12_point,button12_plane)
    app = tk.Tk()
    fig = plt.Figure(figsize=(5, 5), tight_layout=True)
    ax = fig.add_subplot(111, projection='3d')
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    plot_cube(ax)

    button1 = tk.Checkbutton(app, text="OP 평면 구하기",command = OP_plane_event)
    label = tk.Label(app, text="세 점을 입력하세요(x,y,z)")
    entry_point1 = tk.Entry(app)
    entry_point2 = tk.Entry(app)
    entry_point3 = tk.Entry(app)
    button_add_point = tk.Button(app, text="Add point", command=OP_plane)

    label.pack_forget()
    entry_point1.pack_forget()
    entry_point2.pack_forget()
    entry_point3.pack_forget()
    button1.pack()
    button_add_point.pack_forget()

    button2 = tk.Checkbutton(app, text="MP평면 구하기",command=MP_plane_event)
    label2 = tk.Label(app, text="세 점을 입력하세요(x,y,z)")
    entry2_point1 = tk.Entry(app)
    entry2_point2 = tk.Entry(app)
    entry2_point3 = tk.Entry(app)
    button_add_point2 = tk.Button(app, text="Add point", command=MP_plane)

    button2.pack()
    label2.pack_forget()
    entry2_point1.pack_forget()
    entry2_point2.pack_forget()
    entry2_point3.pack_forget()
    button_add_point2.pack_forget()

    button3 = tk.Checkbutton(app, text="FH plane 구하기",command=FH_plane_event)
    fh_label1 = tk.Label(app, text="네 점을 OrR,OrL,PoR,PoL 순으로 입력하세요")
    fh_entry1 = tk.Entry(app)
    fh_entry2 = tk.Entry(app)
    fh_entry3 = tk.Entry(app)
    fh_entry4 = tk.Entry(app)
    button_add_point3 = tk.Button(app, text="Add point", command=FH_plane)

    button3.pack()
    fh_label1.pack_forget()
    fh_entry1.pack_forget()
    fh_entry2.pack_forget()
    fh_entry3.pack_forget()
    fh_entry4.pack_forget()
    button_add_point3.pack_forget()

    button4 = tk.Checkbutton(app, text="YZ plane or SP plane 구하기",command=SP_plane_event)
    sp_label = tk.Label(app,text="N point와 S, FH 평면을 차례대로 입력하세요")
    sp_n_label = tk.Label(app,text="N point를 입력하세요")
    sp_n_entry = tk.Entry(app)
    sp_s_label = tk.Label(app, text="s 점을 입력하세요")
    sp_s_entry = tk.Entry(app)
    sp_plane_label = tk.Label(app, text="FH plane을 입력하세요(a,b,c,d 네 점 입력)")
    sp_plane_entry = tk.Entry(app)
    button_add_point4 = tk.Button(app, text="Add point", command=SP_plane)

    button4.pack()
    sp_label.pack_forget()
    sp_n_label.pack_forget()
    sp_n_entry.pack_forget()
    sp_s_label.pack_forget()
    sp_s_entry.pack_forget()
    sp_plane_label.pack_forget()
    sp_plane_entry.pack_forget()
    button_add_point4.pack_forget()

    button5 = tk.Checkbutton(app, text="XZ plane",command=XZ_plane_event)
    xz_label = tk.Label(app, text="FH plane과 N점을 차례대로 입력하세요")
    plane_label = tk.Label(app,text="FH Plane : a,b,c,d")
    fh_plane_entry = tk.Entry(app)
    xz_n_point_label = tk.Label(app, text="x,y,z")
    xz_n_point_entry = tk.Entry(app)
    button_add_point5 = tk.Button(app, text="Add point", command=XZ_plane)
    button5.pack()
    xz_label.pack_forget()
    plane_label.pack_forget()
    fh_plane_entry.pack_forget()
    xz_n_point_label.pack_forget()
    xz_n_point_entry.pack_forget()
    button_add_point5.pack_forget()

    button6 = tk.Checkbutton(app, text="XY plane",command=XY_plane_event)
    xy_label = tk.Label(app, text="N point와 FH plane, SP plane을 차례대로 입력하세요")
    xy_point_label = tk.Label(app, text="N point 먼저 입력하세요 : x,y,z")
    xy_point_entry = tk.Entry(app)
    xy_fh_plane = tk.Entry(app)
    xy_sp_plane = tk.Entry(app)
    button_add_point6 = tk.Button(app, text="Add point", command=XY_plane)
    button6.pack()
    xy_label.pack_forget()
    xy_point_label.pack_forget()
    xy_point_entry.pack_forget()
    xy_fh_plane.pack_forget()
    xy_sp_plane.pack_forget()
    button_add_point6.pack_forget()

    button7 = tk.Checkbutton(app, text='세 점 사이 각도',command=threee_point_angle_event)
    point_label = tk.Label(app, text="세 점을 차례대로 입력하세요")
    point1_entry = tk.Entry(app)
    point2_entry = tk.Entry(app)
    point3_entry = tk.Entry(app)
    button_add_point7 = tk.Button(app, text="Add point", command=three_point_angle)
    button7.pack()
    point_label.pack_forget()
    point1_entry.pack_forget()
    point2_entry.pack_forget()
    point3_entry.pack_forget()
    button_add_point7.pack_forget()

    button8 = tk.Checkbutton(app, text="u1-SN",command=plane_line_angle_envet)
    line_label = tk.Label(app,text="u1-u1A를 연결해야 합니다. u1과 u1A를 차례대로 입력하세요")
    u1_point_entry = tk.Entry(app)
    u1a_point_entry = tk.Entry(app)
    plane_point = tk.Label(app, text="점 S, N을 지나고 SP에 수직인 평면을 표시할 예정입니다. 두 점을 먼저 입력해주세요")
    s_point_entry = tk.Entry(app)
    n_point_entry = tk.Entry(app)
    sp_plane_label2 = tk.Label(app, text="sp 평면을 입력하세요(a,b,c,d)")
    sp_plane_entry2 = tk.Entry(app)
    button_add_point8 = tk.Button(app, text="Add point", command=plane_line_angle)
    button8.pack()
    line_label.pack_forget()
    u1_point_entry.pack_forget()
    u1a_point_entry.pack_forget()
    plane_point.pack_forget()
    s_point_entry.pack_forget()
    n_point_entry.pack_forget()
    sp_plane_label2.pack_forget()
    sp_plane_entry2.pack_forget()
    button_add_point8.pack_forget()


    button9 = tk.Checkbutton(app, text="L1-L1A연결 직선과 MP평면의 각도",command=plane_line_angle_envet2)
    button9_label = tk.Label(app, text="L1과 L1A를 먼저 차례대로 입력하세요")
    l1 = tk.Entry(app)
    l1a = tk.Entry(app)
    button9_label2 = tk.Label(app, text="MP 평면을 입력하세요(a,b,c,d)")
    mp_plane = tk.Entry(app)
    button_add_point9 = tk.Button(app, text="Add point", command=plane_line_angle2)
    button9.pack()
    button9_label.pack_forget()
    l1.pack_forget()
    l1a.pack_forget()
    button9_label2.pack_forget()
    mp_plane.pack_forget()
    button_add_point9.pack_forget()

    button10 = tk.Checkbutton(app,text="OP-FH",command=OP_and_FH_event)
    button10_label = tk.Label(app, text="OP평면과 FH 평면의 각도를 구해보겠습니다. OP평면 먼저 입력해주세요")
    op_plane = tk.Entry(app)
    fh_plane = tk.Entry(app)
    button_add_point10 = tk.Button(app, text="Add point", command=OP_FH_angle)
    button10.pack()
    button10_label.pack_forget()
    op_plane.pack_forget()
    fh_plane.pack_forget()
    button_add_point10.pack_forget()

    button11 = tk.Checkbutton(app, text="두 점 사이 거리",command=two_point_distance_event)
    button11_label = tk.Label(app, text="두 점을 차례대로 입력하세요")
    button11_point1 = tk.Entry(app)
    button11_point2 = tk.Entry(app)
    button_add_point11 = tk.Button(app, text="Add point", command=two_point_distance)
    button11.pack()
    button11_label.pack_forget()
    button11_point1.pack_forget()
    button11_point2.pack_forget()
    button_add_point11.pack_forget()

    button12 = tk.Checkbutton(app,text="점과 평면 사이 거리",command=point_plane_distance_event)
    button12_label = tk.Label(app, text="점과 평면을 차례대로 입력하세요")
    button12_point = tk.Entry()
    button12_plane = tk.Entry()
    button_add_point12 = tk.Button(app, text="Add point", command=point_plane_distance)
    button12.pack()
    button12_label.pack_forget()
    button12_point.pack_forget()
    button12_plane.pack_forget()
    button_add_point12.pack_forget()

    #plot 초기화 버튼
    delete_button = tk.Button(app, text="plot 초기화 버튼",command=delete)
    delete_button.pack(side=tk.BOTTOM)
    #코드 실행
    app.mainloop()
main()