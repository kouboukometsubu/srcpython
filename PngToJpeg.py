import cv2
import sys
#sys.path.append("..\GClass")
import GClass.TakanoFileManager as fileManager

# PNG画像を読み込む
pngImg = input("filename=")
image = cv2.imread(pngImg)

jpgImg = fileManager.GetFileName(pngImg) + ".jpg"

print(jpgImg)

# JPG画像として保存する
cv2.imwrite(jpgImg, pngImg, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
