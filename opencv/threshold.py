import cv2
import sys

sys.path.append("D:/srcpython/opencv")

filename = "D:/srcpython/opencv/test.bmp"
#filename = "test.bmp"

img = cv2.imread(filename)  # flagsは省略（デフォ値＝1）

if img is None:
    print( "read error")
else:
    print(img.size)

    #img2 = cv2.GaussianBlur(img, [5,5], 10, 10)
    img2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("image", img2)




    cv2.waitKey()