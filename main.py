import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
time.sleep(3)

background = 0

for i in range(30):
    ret, background = video.read()

    background = np.flip(background, axis=1)


while True:
    ret, img = video.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (35, 35), 0)

    lower = np.array([20, 120, 60])
    upper = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower, upper)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1 + mask2

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(mask==255)] = background[np.where(mask==255)]


    cv2.imshow("Display", img)

    k = cv2.waitKey(1)
    if k==ord('q'):
        break

video.realease()
cv2.destroyAllWindows()