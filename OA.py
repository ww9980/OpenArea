import cv2
import numpy as np
img = cv2.imread('1.jpg')
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('image',bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
colors, counts = np.unique(bw_img.reshape(-1, 3),axis=0,return_counts=True)
OA = counts[0]/(np.sum(counts))
print(OA)