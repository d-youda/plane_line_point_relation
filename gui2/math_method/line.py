import numpy as np
import math
def slove_line_and_plane_angle(plane, line):
    #plane은 [a,b,c,d]형태의 입력, line은 [[a,b,c], [d,e,f]] 형태의 입력
    #plane : ax+by+cz=d | line : 두 점을 지나는 직선

    #1. 평면의 법선벡터 구하기
    plane_n_vec = np.array([plane[0], plane[1], plane[2]])
    plane_n_vec = np.linalg.norm(plane_n_vec)
    #2. 직선의 방향벡터 구하기
    #2-1 직선 상의 두 점 구하기
    point1 = line[0]
    point2 = line[1]
    line_dir_vec = point2-point1
    line_dir_vec = np.linalg.norm(line_dir_vec)

    #3. 두 벡터의 내적 계산
    dot_product = np.dot(line_dir_vec, plane_n_vec)
    #4.cos theta값
    theta = dot_product/(line_dir_vec*plane_n_vec)
    #5.cos 제외 tehta값 ->라디안 값으로 출력됨
    radian = np.arccos(theta)
    #6.라디안을 각도로 바꿈
    degree = math.degrees(radian)
    return degree