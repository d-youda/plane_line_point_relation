from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_cube(ax):
    # 큐브 그리기
    vertices = [
        [-10, -10, -10], [10, -10, -10], [10, 10, -10], [-10, 10, -10],
        [-10, -10, 10], [10, -10, 10], [10, 10, 10], [-10, 10, 10]
    ]

    # 정육면체 만들기
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[7], vertices[6], vertices[2], vertices[3]],
        [vertices[0], vertices[4], vertices[7], vertices[3]],
        [vertices[1], vertices[5], vertices[6], vertices[2]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[2], vertices[3]]
    ]

    # Plot the cube by creating a Poly3DCollection of the faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='gray', linewidths=1, edgecolors='black', alpha=0.5))

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

def update_cube(ax, a,b,c):
    # 방정식 입력받았을 때, 화면에 평면 그려주는 함수
    try:
        a = int(a.get())
        b = int(b.get())
        c = int(c.get())

        x,y = np.meshgrid(range(-10,10), range(-10,10))
        z = (-a*x -b*y)/c

        ax.plot_surface(x,y,z, color='red')
        ax.set_xlabel(f"{a}x+{b}y+{c}z = 0")

        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])

    except ValueError:
        print("Invalid input for a, b, or c")