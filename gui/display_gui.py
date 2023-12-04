import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from plot_cube import plot_cube,update_cube
from button_frame import create_button_frame
from enter_the_eqation import enter_the_equation
root = tk.Tk()
root.title("시각화 화면")

#tk 화면에 뿌려주기 위해 canvas 생성
fig = plt.Figure(figsize=(5, 5), tight_layout=True)
ax = fig.add_subplot(111, projection='3d') #3d 정육면체 만들기
canvas = FigureCanvasTkAgg(fig,master=root) #화면에 정육면체 넣을 캔버스 그리기
canvas_width = canvas.get_tk_widget()
canvas_width.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
plot_cube(ax) #cube 그리기

button_frame = create_button_frame(root)
button_frame.pack(side=tk.RIGHT, fill=tk.Y)

#방정식 입력받을 화면 만들기
#a,b,c 입력받기
equation_label = tk.Label(root, text="평면의 방정식을 입력하세요(ax+by+c=0의 형태)")
a = enter_the_equation(root,'a')
b = enter_the_equation(root,'b')
c = enter_the_equation(root,'c')
#입력완료 버튼
update_button = tk.Button(root, text='평면 그리기',
                          command=lambda:update_cube(ax,a,b,c))
update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#화면에 뿌리기
root.mainloop() 