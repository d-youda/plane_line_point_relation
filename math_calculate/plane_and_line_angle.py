#평면과 직선이 이루는 각도 구하는 소스
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
def slove_line_and_plane_angle(plane, line):
    #plane은 [a,b,c,d]형태의 입력, line은 [[a,b,c], [d,e,f]] 형태의 입력
    #plane : ax+by+cz=d | line : 두 점을 지나는 직선

    #1. 평면의 법선벡터 구하기
    plane_n_vec = np.array([plane[0], plane[1], plane[2]])
    plane_n_vec = np.linalg.norm(plane_n_vec)
    #2. 직선의 방향벡터 구하기
    #2-1 직선 상의 두 점 구하기
    point1 = line[0]
    point2 = line[1]
    line_dir_vec = point2-point1
    line_dir_vec = np.linalg.norm(line_dir_vec)

    #3. 두 벡터의 내적 계산
    dot_product = np.dot(line_dir_vec, plane_n_vec)
    #4.cos theta값
    theta = dot_product/(line_dir_vec*plane_n_vec)
    #5.cos 제외 tehta값 ->라디안 값으로 출력됨
    radian = np.arccos(theta)
    #6.라디안을 각도로 바꿈
    degree = math.degrees(radian)
    return degree

total_x ,total_y = np.meshgrid(range(-10,10),range(-10,10))
total_z = total_x
fig=plt.figure()
ax = fig.add_subplot(111,projection='3d') #plot 3차원으로 나타내기
ax.plot_surface(total_x,total_y,total_z)
plt.show()

plane = np.array(list(map(int,input("평면을 입력하세요(ax+by+cz=d에서의 a,b,c,d만 입력하시면 됩니다.):").split(","))))
print("직선이 지나갈 두 점을 입력하세요")
line_point1 = np.array(list(map(int, input("point1(x,y,z형태 입력): ").split(","))))
line_point2 = np.array(list(map(int, input("point2(x,y,z형태 입력): ").split(","))))
line = [line_point1,line_point2]
#직선과 평면 시각화
a,b,c,d = plane
plane_x, plane_y = np.meshgrid(range(-10, 10), range(-10, 10)) #10x10 array 두 개 (평면의 x,y)
plane_z = (d - a*plane_x - b*plane_y)/c
print("직선과 평면이 그리는 각도:%d"%(slove_line_and_plane_angle(plane,line )))


ax.plot((line_point1[0],line_point1[1],line_point1[2]),(line_point2[0],line_point2[1],line_point2[2]),color='red', label='line')
ax.legend()
ax.plot_surface(plane_x,plane_y,plane_z, alpha=0.5)
