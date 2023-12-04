import numpy as np
import math

def three_point_plane(point1, point2, point3):
    point1 = np.array(point1)
    point2 = np.array(point2)
    point3 = np.array(point3)
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

    # nomal vector의 요소들은 방정식의 계수들.
    A, B, C = normal_vector

    return A, B, C

def two_plane_angle(plane1, plane2):
    a1,b1,c1 = plane1 # 법선벡터
    a2,b2,c2 = plane2 # 법선벡터
    answer = (a1*a2+b1*b2+c1*c2)/(np.sqrt(a1**2+b1**2+c1**2) * np.sqrt(a2**2+b2**2+c2**2)) #각도 찾기
    theta = math.acos(answer) #acosine으로 각도 측정
    theta_degrees = math.degrees(theta) #라디안 값을 각도로 변환
    return theta_degrees