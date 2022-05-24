import numpy as np
import cv2
from insightface.app import FaceAnalysis
 
image_file = "D:/srcpython/opencv/1.jpg"
img = cv2.imread(image_file)
 
app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))
 
faces = app.get(np.asarray(img))
print("faces:" + str(len(faces)))
 
rimg = app.draw_on(img, faces)
cv2.imwrite("D:/srcpython/opencv/out2.jpg", rimg)