import cv2
import numpy as np
import math

def find_contours(capImg, color):
    img_hsv = cv2.cvtColor(capImg, cv2.COLOR_BGR2GRAY)
    img_mask = cv2.inRange(img_hsv, color[0], color[1])
    contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

color = (
            (30, 80, 0),
            (70, 200, 255)
        )

capImg = cv2.VideoCapture(0)
contours = find_contours(capImg, color)


while(True):
    ret, frame = capImg.read()
    cv2.imshow('Video', frame)
    if contours:
        for cnt in contours:
            if cv2.contourArea(cnt) < 50:
                continue
        
            cv2.drawContours(capImg, [cnt], 0, (255,255,255), 2)
       
        
            triangle = cv2.minEnclosingTriangle(cnt)[1]
            triangle = np.int0(triangle)
            triangle_area = cv2.contourArea(triangle)
            cv2.drawContours(capImg, [triangle], 0, (100,255,150), 2)



    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break
capImg.release()
cv2.destroyAllWindows()