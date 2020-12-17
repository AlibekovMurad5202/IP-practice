import numpy as np 
import os 
import cv2 as cv

def canny(img, weak_th = None, strong_th = None): 
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    img = # НАШ ГАУСС cv.GaussianBlur(img, (3, 3), 1.4) # 5 5 1.4
    
    gx = # НАШ СОБЕЛЬ cv.Sobel(np.float32(img), cv.CV_64F, 1, 0, 3)
    gy = # НАШ СОБЕЛЬ cv.Sobel(np.float32(img), cv.CV_64F, 0, 1, 3)

    # ПЕРЕВОД В ПОЛЯРНЫЕ mag, ang = cv.cartToPolar(gx, gy, angleInDegrees = True) 
    mag_max = np.max(mag) 
    
    if not weak_th:weak_th = mag_max * 0.09 # 0.1
    if not strong_th:strong_th = mag_max * 0.17 # 0.5

    height, width = img.shape 
    for i_x in range(width): 
        for i_y in range(height): 
            grad_ang = ang[i_y, i_x] 
            grad_ang = abs(grad_ang-180) if abs(grad_ang)>180 else abs(grad_ang) 
            if grad_ang<= 22.5: 
                neighb_1_x, neighb_1_y = i_x-1, i_y 
                neighb_2_x, neighb_2_y = i_x + 1, i_y 
            elif grad_ang>22.5 and grad_ang<=(22.5 + 45): 
                neighb_1_x, neighb_1_y = i_x-1, i_y-1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
            elif grad_ang>(22.5 + 45) and grad_ang<=(22.5 + 90): 
                neighb_1_x, neighb_1_y = i_x, i_y-1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
            elif grad_ang>(22.5 + 90) and grad_ang<=(22.5 + 135): 
                neighb_1_x, neighb_1_y = i_x-1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y-1
            elif grad_ang>(22.5 + 135) and grad_ang<=(22.5 + 180): 
                neighb_1_x, neighb_1_y = i_x-1, i_y 
                neighb_2_x, neighb_2_y = i_x + 1, i_y 
            if width>neighb_1_x>= 0 and height>neighb_1_y>= 0: 
                if mag[i_y, i_x]<mag[neighb_1_y, neighb_1_x]: 
                    mag[i_y, i_x]= 0
                    continue
            if width>neighb_2_x>= 0 and height>neighb_2_y>= 0: 
                if mag[i_y, i_x]<mag[neighb_2_y, neighb_2_x]: 
                    mag[i_y, i_x]= 0
   

    for i_x in range(width): 
        for i_y in range(height):
              
            grad_mag = mag[i_y, i_x]
            if grad_mag<weak_th: 
                mag[i_y, i_x]= 0
            elif strong_th>grad_mag>= weak_th: 
                mag[i_y, i_x]= 127
            else: 
                mag[i_y, i_x]= 255
    for i_x in range(1, width - 1): 
        for i_y in range(1, height - 1):
            if (mag[i_y, i_x] == 127):
                if ((mag[i_y-1, i_x-1] == 255) or (mag[i_y-1, i_x] == 255) or (mag[i_y-1, i_x+1] == 255) or
                    (mag[i_y+1, i_x-1] == 255) or (mag[i_y+1, i_x] == 255) or (mag[i_y+1, i_x+1] == 255) or
                    (mag[i_y, i_x-1] == 255) or (mag[i_y, i_x+1] == 255)):
                    mag[i_y, i_x] = 255
                else:
                    mag[i_y, i_x] = 0

    return mag

frame = cv.imread("C:/Users/Zerus/Desktop/234.png") 
canny_img = Canny_detector(frame)
cv.imshow("canny_img", canny_img)
cv.waitKey(0)
cv.destroyAllWindows()
