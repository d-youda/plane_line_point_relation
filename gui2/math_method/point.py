import numpy as np

def two_point_distance(point1, point2):
    answer = np.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    return answer
    
def point_and_plane_distance(point,plane):
    a,b,c = plane
    x,y,z = point
    answer = (a*x+b*y+c*z)/(np.sqrt(a**2+b**2+c**2))
    return answer