import cv2

filename = "D:\map.bmp"
imgCV = cv2.imread(filename)  # flagsは省略（デフォ値＝1）
cv2.imshow("color", imgCV)

cv2.waitKey()
cv2.destroyAllWindows()

imgGray = cv2.cvtColor(imgCV, cv2.COLOR_BGR2GRAY)  # RGB2〜 でなく BGR2〜 を指定
cv2.imshow("gray", imgGray)

cv2.waitKey()

cv2.destroyAllWindows()
exit
