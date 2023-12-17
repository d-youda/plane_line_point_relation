import numpy as np
import math

def three_point_plane(point1, point2, point3):
    '''세 점을 지나는 평면의 방정식 구하기'''
    v1 = point2-point1
    v2 = point3-point1

    # v1,v2 벡터곱 하여 구하고자 하는 평면의 법선벡터(n vector) 구하기
    normal_vector = np.cross(v1, v2) #v1, v2 벡터곱
    # nomal vector의 요소들은 방정식의 계수들.
    A, B, C = normal_vector
    # 평면 방정식의 상수 D 구하기
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
    plane_n_vec = plane[:3]
    v1 = point1-point2
    v2 = point1-plane_n_vec
    n_vector = np.cross(v1,v2)
    a,b,c = n_vector
    d = a*point2[0] +b*point2[1]+c*point2[2]
    answer_plane = a,b,c,d
    return answer_plane

def two_plane_one_point(point,plane1,plane2):
    '''두 평면과 수직이면서, 한 점을 지나는 평면의 방정식 구하기'''
    v1 = plane1[:3]
    v2 = plane2[:3]
    n_vector = np.cross(v1,v2)
    a,b,c = n_vector
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane

def one_parallel_plane_and_point(plane,point):
    '''한 평면과 평행하면서, 한 점을 지나는 평면의 방정식 구하기'''
    n_vector = plane[:3]
    a,b,c = n_vector
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane