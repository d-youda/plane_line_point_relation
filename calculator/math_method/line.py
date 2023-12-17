import numpy as np
import math
def slove_line_and_plane_angle(plane,line_point1,line_point2):
    #plane은 [a,b,c,d]형태의 입력, line은 [[a,b,c], [d,e,f]] 형태의 입력
    #plane : ax+by+cz=d | line : 두 점을 지나는 직선

    #1. 평면의 법선벡터 구하기
    plane_n_vec = np.array(plane[:3])
    #2. 두 점이 만드는 직선의 방향벡터 구하기
    line_dir_vec = line_point2-line_point1 
    
    #3. 두 벡터의 내적 계산
    dot_product = np.dot(line_dir_vec, plane_n_vec)
    #4.cos theta값
    norm1 = np.linalg.norm(line_dir_vec)
    norm2 = np.linalg.norm(plane_n_vec)    
    cos_theta = dot_product/(norm1*norm2)
    radian = np.arccos(cos_theta)
    degree = np.degrees(radian)
    return degree

def solve_two_line_angle(dir_vector1, dir_vector2):
    dot_product = np.dot(dir_vector1,dir_vector2) #두 벡터 내적
    norm1 = np.linalg.norm(dir_vector1)
    norm2 = np.linalg.norm(dir_vector2)

    cos_theta = dot_product/(norm1*norm2)
    radian = np.arccos(cos_theta)
    degree = np.degrees(radian)
    return degree