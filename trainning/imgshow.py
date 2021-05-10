import cv2

img = cv2.imread("D:\region.bmp", 1 )
cv2.imshow("img", img )
cv2.waitKey(1)
cv2.destroyAllwindows()
