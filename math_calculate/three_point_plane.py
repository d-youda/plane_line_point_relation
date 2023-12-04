'''세 점을 지나는 평면 구하기'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def three_point_search_plane(point1, point2, point3):
    '''세 점이 주어졌을 때, 평면 찾기'''
    #1. 기준점으로 잡을 원점과 가장 가까운 점 구하기
    o = np.array([0,0,0])
    #1-1. 점과 점 사이 거리 구하기
    o_point1 = np.sqrt(((point1[0]-o[0])**2) + ((point1[1]-o[1])**2) + ((point1[2]-o[2])**2))
    o_point2 = np.sqrt(((point2[0]-o[0])**2) + ((point2[1]-o[1])**2) + ((point2[2]-o[2])**2))
    o_point3 = np.sqrt(((point3[0]-o[0])**2) + ((point3[1]-o[1])**2) + ((point3[2]-o[2])**2))

    #1-2. 거리 가장 작은 애를 기준점으로 지정하기
    if (o_point1 <= o_point2) and (o_point1 <= o_point3):
        stand_point = point1
        non_stand1 = point2
        non_stand2 = point3
    elif (o_point2 <= o_point1) and (o_point2 <= o_point3) :
        stand_point = point2
        non_stand1 = point1
        non_stand2 = point3
    elif (o_point3 <= o_point1) and (o_point3 <= o_point2):
        stand_point = point3
        non_stand1 = point1
        non_stand2 = point2

    # 2. 구한 기준점을 사용하여 법선 벡터를 구하기 위해, 두 벡터 구하기
    v1 = non_stand1 - stand_point
    v2 = non_stand2 - stand_point

    # v1,v2 벡터곱 하여 구하고자 하는 평면의 법선벡터(n vector) 구하기
    normal_vector = np.cross(v1, v2) #v1, v2 벡터곱

    # 평면 방정식의 상수 D 구하기
    D = np.dot(normal_vector, stand_point)#내적(dot product)

    # nomal vector의 요소들은 방정식의 계수들.
    A, B, C = normal_vector

    return A, B, C ,D

# 세 점 입력받기
#point1 = np.array([0,0,0])
#point2 = np.array([2,4,6])
#point3 = np.array([-1,2,7])
def plot_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the eight vertices of the cube
    vertices = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ]

    # Define the six faces of the cube using the vertices
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[7], vertices[6], vertices[2], vertices[3]],
        [vertices[0], vertices[4], vertices[7], vertices[3]],
        [vertices[1], vertices[5], vertices[6], vertices[2]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[2], vertices[3]]
    ]

    # Plot the cube by creating a Poly3DCollection of the faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='gray', linewidths=1, edgecolors='b', alpha=0.5))

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot limits
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Show the plot
    plt.show()

# Call the function to plot the cube
plot_cube()
#파이썬에서 input은 모두 string 형태로 받기 때문에, map함수를 사용하여 input을 받음과 동시에 int형들이 들어간 list로 변환해줌
point1 = np.array(list(map(int, input("point1(x,y,z):").split(","))))
point2 = np.array(list(map(int,input("point2(x,y,z):").split(","))))
point3 = np.array(list(map(int,input("point3(x,y,z):").split(","))))

# 위에서 정의한 함수를 사용하여 평면 방정식을 구합니다.
A,B,C,D = three_point_search_plane(point1, point2, point3)
print(f"평면의 방정식 | {A}x+{B}y+{C}z={D}")
#x,y값 면적 전체로 설정하기(일단 무작위 설정함.)
x, y = np.meshgrid(range(-10, 10), range(-10, 10)) #10x10 array 두 개 
z = (D- A*x - B*y)/C #Ax+By+Cz = D를 풀어, z 구함

#구한 평면 방정식을 평면에 나타냅니다. (시각화)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(point1[0],point1[1],point1[2],color="red",label='point1')
ax.scatter(point2[0],point2[1],point2[2],color="green",label='point2')
ax.scatter(point3[0],point3[1],point3[2],color="blue",label='point3')
ax.legend()
plt.title(f"평면: {A}x + {B}y + {C}z = {D}")
ax.plot_surface(x,y,z,alpha=0.5)
plt.show()