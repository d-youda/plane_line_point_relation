import numpy as np
import math
def two_point_distance(point1, point2):
    #두 점의 거리 = 두 점을 이은 벡터의 크기와 같다.
    distance = np.linalg.norm(np.array(point2) - np.array(point1))
    return distance
def overjet(point1,point2):
    #overjet은 두 점의 y축에서의 거리와 같다.
    y1 = point1[1]
    y2 = point2[1]
    distance = np.abs(y2-y1)
    return distance

def overbite(point1,point2):
    #overbite는 두 점의 z축에서의 거리와 같다.
    z1 = point1[2]
    z2 = point2[2]
    distance = np.abs(z2-z1)
    return distance

def point_and_plane_distance(point,plane):
    a,b,c,d = plane
    x,y,z = point
    distance = np.abs(a * x + b* y + c * z - d) /  np.sqrt(a*a + b*b + c*c)
    return distance

def three_point_angle_solve(point1, point2, point3):
    v1 = point1-point2
    v2 = point1-point3

    dot_product = np.dot(v1,v2)
    #벡터 크기 계산
    v1_mag = np.linalg.norm(v1)
    v2_mag = np.linalg.norm(v2)

    #각도
    cosine_theta = dot_product/(v1_mag*v2_mag)
    #라디안 각도 구하기
    theta = np.arccos(cosine_theta)
    #도로 변환
    degree = np.degrees(theta)
    return degree

def middle_two_point(point1, point2):
    '''두 점의 중간에 있는 점 구하기'''
    middle_point = np.array([(point1[0]+point2[0])/2,(point1[1]+point2[1])/2,(point1[2]+point2[2])/2])
    return middle_point