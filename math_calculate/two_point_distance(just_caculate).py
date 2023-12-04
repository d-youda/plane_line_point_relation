import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#두 점 사이 거리 구하기
#sagittal(관상면) -> 어느 축 하나를 기준으로.. 삼아야 함
def find_distance(point1, point2):
    answer = np.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    return answer

point1 = np.array(list(map(int,input("첫 번째 point(x,y,z): ").split(","))))
point2 = np.array(list(map(int,input("두 번째 point(x,y,z): ").split(","))))


print(f"{point1}과 ({point2}) 사이 거리 : {find_distance(point1,point2)}")

#두 점 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') #3차원으로 변경
ax.scatter(point1[0], point1[1], point1[2],color='red',label='point1')
ax.scatter(point2[0], point2[1], point2[2], color='blue',label='point2')
ax.legend()
plt.show()