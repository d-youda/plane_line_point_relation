import numpy as np
from math import gcd

def three_point_plane(point1, point2, point3):
    '''세 점을 지나는 평면의 방정식 구하기'''
    #1. 두 점을 지나는 벡터 각각 구하기
    v1 = point2-point1
    v2 = point3-point1

    #2. 법선벡터는 v1과 v2 동시에 수직이기 때문에 n_vec = v1 x v2
    normal_vector = np.cross(v1, v2) #v1, v2 벡터곱
    normal_vector //=slove_GCD(normal_vector) #법선벡터 최대한 작게 만들기
    
    #3. 법선벡터는 해당 평면의 방정식의 계수들을 의미한다
    A, B, C = normal_vector

    #4. 평면 방정식의 상수 D 구하기
    D = A*point1[0] + B*point1[1]+ C*point1[2]

    return A, B, C ,D

def two_plane_angle(plane1, plane2):
    '''두 평면이 이루는 각 구하기'''
    n_vec1 = plane1[:3]
    n_vec2 = plane2[:3]
    dot_product = np.dot(n_vec1,n_vec1)

    #두 벡터 크기
    n_vec1_mag = np.linalg.norm(n_vec1)
    n_vec2_mag = np.linalg.norm(n_vec2)

    #라디안 각도 계산
    cosine_theta = dot_product/(n_vec1_mag*n_vec2_mag)
    theta = np.arccos(cosine_theta)
    degree = np.degrees(theta)
    return degree

def two_point_one_plane(point1,point2,plane):
    '''두 점을 지나며, 한 평면과 수직인 다른 한 평면의 방정식 구하기'''
    #1. 두 점을 통과하는 벡터 구하기
    vector = point2-point1
    #평면의 nomal vector를 사용하여 두 점을 통과하는 평면의 n vector
    n_vector //=slove_GCD(n_vector)

    a,b,c = n_vector
    d = a*point2[0] +b*point2[1]+c*point2[2]
    answer_plane = a,b,c,d
    return answer_plane

def two_plane_one_point(point,plane1,plane2):
    '''두 평면과 수직이면서, 한 점을 지나는 평면의 방정식 구하기'''
    v1 = plane1[:3]
    v2 = plane2[:3]
    n_vector = np.cross(v1,v2)
    n_vector //=slove_GCD(n_vector)

    a,b,c = n_vector
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane

def one_parallel_plane_and_point(plane,point):
    '''한 평면과 평행하면서, 한 점을 지나는 평면의 방정식 구하기'''
    n_vector = plane[:3]
    # n_vector //=slove_GCD(n_vector)
    a,b,c = n_vector
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane

def slove_GCD(vector):
    '''
    법선벡터는 방향벡터를 의미하기 때문에 크기가 중요하지 않다.
    따라서 법선벡터를 최대한 간단한 식으로 나타내기 위해 최대공약수를 구해
    약분을 진행한다.
    '''
    x,y,z = vector
    x = int(x)
    y = int(y)
    z = int(z)
    x_y = gcd(x,y)
    x_y_z = gcd(x_y,z)
    return x_y_z