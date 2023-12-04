import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#주의점 : math 모듈에서의 값은 모두 라디안 값 기준. 
def two_line_angle(line1, line2):
    #1. 두 직선의 방향벡터 각각 구하기
    directional_vector1 = line1[1] - line1[0]
    directional_vector2 = line2[1] - line2[0]
    #2. 각도 구하기
    dot_product = np.dot(directional_vector1,directional_vector2)
    cosine_theta = dot_product/(np.linalg.norm(directional_vector1) * np.linalg.norm(directional_vector2))
    #theta값 구하기
    theta = np.arccos(cosine_theta)
    #각도 구하기
    degree = np.degrees(theta)
    return degree
#직선을 그리기 위한 두 점 입력받기
print("첫 번째 직선이 지나갈 두 점을 입력하세요")
line1_point1 = np.array(list(map(int, input("point1(x,y,z형태 입력): ").split(","))))
line1_point2 = np.array(list(map(int, input("point2(x,y,z형태 입력): ").split(","))))
line1 = [line1_point1,line1_point2]

print("두 번째 직선이 지나갈 두 점을 입력하세요")
line2_point1 = np.array(list(map(int, input("point1(x,y,z형태 입력): ").split(","))))
line2_point2 = np.array(list(map(int, input("point2(x,y,z형태 입력): ").split(","))))
line2 = [line2_point1,line2_point2]

degree = two_line_angle(line1, line2)
print("두 직선이 이루는 각도:%d"%(degree))

#두 직선 시각화
fig=plt.figure()
ax = fig.add_subplot(111,projection='3d') #plot 3차원으로 나타내기
ax.plot((line1_point1[0],line1_point1[1],line1_point1[2]),(line1_point2[0],line1_point2[1],line1_point2[2]),color='red', label='line1')
ax.plot((line2_point1[0],line2_point1[1],line2_point1[2]),(line2_point2[0],line2_point2[1],line2_point2[2]),color='red', label='line2')
ax.legend()
plt.show()