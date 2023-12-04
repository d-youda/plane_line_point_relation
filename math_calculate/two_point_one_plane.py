import numpy as np
import matplotlib.pyplot as plt
'''두 점을 지나면서, 한 평면에 수직인 평면 구하기'''
def two_spot_one_plane(point1, point2, plane):
    #1. point1과 point2의 방향 벡터 구함
    directional_vector = point2-point1
    a,b,c,d = plane
    #2. 수직인 평면의 norm vector
    normal_vector = np.array([a,b,c])
    #3. 두 벡터 외적
    answer_normal_vector = np.cross(directional_vector,normal_vector)
    return answer_normal_vector
        
#시각화
point1 = np.array([1,2,3])
point2 = np.array([8,10,12])

x , y =np.meshgrid(range(-10,10), range(-10,10))
#평면 방정식 : 16x+20y+8z = 20
z = (5 - 16*x -20*y)/8
plane = [2,10,3,20]
new_plane = two_spot_one_plane(point1, point2,plane)
a,b,c = new_plane
d = plane[0]*a+plane[1]*b+plane[2]*c
new_plane_z = (d-a*x-b*y)/c

print(f"새 평면:{a}x+{b}y+{c}z={d}")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(point1[0],point1[1],point1[2],color="red",label='point1')
ax.scatter(point2[0],point2[1],point2[2],color="green",label='point2')
ax.legend()
plt.title(f"평면: 16x+20y+8z = 0")
ax.plot_surface(x,y,z,alpha=0.5,color='blue')
ax.plot_surface(x,y,new_plane_z, alpha=0.5, color='red')
plt.show()