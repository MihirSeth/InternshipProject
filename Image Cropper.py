import cv2
import numpy as np
#img = cv2.imread("test.png")
from Classifier import classifier


filenames = "PAN.jpeg"
img = cv2.imread(filenames)
blurred = cv2.blur(img, (3,3))
canny = cv2.Canny(blurred, 50, 200)

## find the non-zero min-max coords of canny
pts = np.argwhere(canny>0)
y1,x1 = pts.min(axis=0)
y2,x2 = pts.max(axis=0)

## crop the region
cropped = img[y1:y2, x1:x2]

filename_cropped = filenames.split('.')
filename_cropped[0] = filename_cropped[0] + '_cropped'
filename_cropped = '.'.join(filename_cropped)

cv2.imwrite(filename_cropped, cropped)

tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
cv2.imshow("tagged", tagged)
# cv2.waitKey()

classifier(filename_cropped)

