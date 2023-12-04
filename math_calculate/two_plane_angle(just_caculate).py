import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
#두 평면이 이루는 각도 구하기
#두 평면이 이루는 각도는 각각 평면의 법선 벡터가 이루는 각도와 같다.
def find_angle_with_two_plane(plane1, plane2):
    a1,b1,c1,d1 = plane1 # 법선벡터
    a2,b2,c2,d2 = plane2 # 법선벡터
    answer = (a1*a2+b1*b2+c1*c2)/(np.sqrt(a1**2+b1**2+c1**2) * np.sqrt(a2**2+b2**2+c2**2)) #각도 찾기
    theta = math.acos(answer) #acosine으로 각도 측정
    theta_degrees = math.degrees(theta) #라디안 값을 각도로 변환
    return theta_degrees

plane1 = np.array(list(map(int,input("첫 번째 평면의 방정식(ax_by+cz=d에서 a,b,c,d): ").split(","))))
plane2 = np.array(list(map(int,input("두 번째 평면의 방정식(ax_by+cz=d에서 a,b,c,d): ").split(","))))

a1,b1,c1,d1 = plane1
a2,b2,c2,d2 = plane2

answer = find_angle_with_two_plane(plane1=plane1, plane2=plane2)
print("평면 %dx+%dy+%dz = %d와 %dx+%dy+%dz = %d 사이의 각도(예각 기준):%d"%(a1,b1,c1,d1,a2,b2,c2,d2,answer))

#두 평면 겹치는 것 시각화
x, y = np.meshgrid(range(-10, 10), range(-10, 10)) #10x10 array 두 개 
first_equation_z = (d1-a1*x-b1*y)/c1
second_equation_z = (d2-a2*x-b2*y)/c2

fig=plt.figure()
ax = fig.add_subplot(111,projection='3d') #plot 3차원으로 나타내기
ax.plot_surface(x,y,first_equation_z,alpha=0.5,color='red',label=f'{a1}x+{b1}y+{c1}z = {d1}')
ax.plot_surface(x,y,second_equation_z,alpha=0.5,color='blue', label=f'{a2}x+{b2}y+{c2}z = {d2}')
# ax.legend()

# ax.legend()
plt.show()