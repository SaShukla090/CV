import argparse 
import cv2

import numpy as np
image = np.random.randint(0,255,(1080,1080,3))
# image1 = np.random.normal(125,90,(1080,1080,3))

# cap = cv2.VideoCapture(0)
# success, image = cap.read()
# cap.release()

# print(image.shape)
# cv2.imshow("image", cv2.flip(image,1))
import matplotlib.pyplot as plt
plt.imshow(image)
plt.waitforbuttonpress()
print("10")