import numpy as np

def three_point_plane(point1, point2, point3):
    '''세 점을 지나는 평면의 방정식 구하기'''
    #1. 두 점을 지나는 벡터 각각 구하기
    v1 = point2-point1
    v2 = point3-point1

    #2. 법선벡터는 v1과 v2 동시에 수직이기 때문에 n_vec = v1 x v2
    normal_vector = np.cross(v1, v2) #v1, v2 벡터곱
    
    #3. 법선벡터는 해당 평면의 방정식의 계수들을 의미한다
    A, B, C = normal_vector

    #4. 평면 방정식의 상수 D 구하기
    D = A*point1[0] + B*point1[1]+ C*point1[2]

    return A, B, C ,D

def two_plane_angle(plane1, plane2):
    '''두 평면이 이루는 각 구하기'''
    a,b,c,d = plane1
    a1,b1,c1,d1 = plane2
    cosine_theta = (np.abs(a*a1+b*b1+c*c1))/((np.sqrt(a*a+b*b+c*c))*(np.sqrt(a1*a1+b1*b1+c1*c1)))
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
    #1. 주어진 평면에서 상수d를 제외하면 법선벡터를 나타냄
    direction_vector1 = plane1[:3]
    direction_vector2 = plane2[:3]

    #2.두 벡터와 동시에 수직인 벡터 = 구하고자 하는 평면의 법선벡터
    n_vector = np.cross(direction_vector1,direction_vector2)

    #3. 평의 방정식의 계수이자 평면의 법선벡터
    a,b,c = n_vector
    #4. 점 대입하여 상수 구함
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane

def one_parallel_plane_and_point(plane,point):
    '''한 평면과 평행하면서, 한 점을 지나는 평면의 방정식 구하기'''
    #1. 평행하는 평면은 같은 법선벡터 가짐
    n_vector = plane[:3]
    # n_vector //=slove_GCD(n_vector)
    a,b,c = n_vector
    #2. 점을 대입하여 상수 구함
    d = a*point[0] +b*point[1]+c*point[2]
    answer_plane = a,b,c,d
    return answer_plane

