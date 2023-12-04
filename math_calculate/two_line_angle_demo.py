import cv2
import numpy as np
# 두 라인의 각도 계산
def mouse_event(event, x, y, flags, param):
    global count, pre_x, pre_y

    if event==cv2.EVENT_FLAG_LBUTTON:
        count = count+1
        if count%2 == 0:
            #두 번 이상 클릭했을 경우
            cv2.circle(img, (x,y), 5, (255,0,0), -1) #시작점 파란색
            cv2.line(img,(pre_x,pre_y), (x,y), (255,255,255),2) #선 그리기
            list_vector.append(np.array([x-pre_x, y-pre_y]))

            if len(list_vector)==2:
                radian = np.arccos(np.dot(list_vector[0],list_vector[1])/(np.linalg.norm(list_vector[0])*np.linalg.norm(list_vector[1]))) #acos 연산
                theta = (radian*180)/np.pi
                theta = np.fmin(theta, 180.0-theta) #작은 각으로 출력해줌

                print(theta) 
                count = 0
                list_vector.clear()
        else:
            pre_x = x
            pre_y = y
            cv2.circle(img, (x,y), 5, (0,0,255), -1) #끝점 빨간색

image_empty = np.zeros((1000,1000,3), dtype=np.uint8)
img = image_empty.copy()
count = 0
pre_x = -1
pre_y = -1
list_vector = []

while True:
    text1 = "if you want clean screen, push your space bar."
    text2 = "if you want this program exit, push your esc key"
    cv2.putText(img,text1,(20,50), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),1)
    cv2.putText(img,text2,(20,80), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),1)

    cv2.imshow('set location', img)
    cv2.setMouseCallback("set location", mouse_event, img)

    key = cv2.waitKey(1)
    if key == 27: #ESC 입력 시 종료
        break 
    elif key==32: #space bar push-> 깨끗한 화면
        img = image_empty.copy()