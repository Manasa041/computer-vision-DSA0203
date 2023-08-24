import cv2
import numpy as np

def sharpen_image_high_boost(image, alpha):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    final_image = cv2.addWeighted(image, 1 + alpha, sharpened_image, -alpha, 0)

    return final_image
image_path = "C:/Users/Acer/Pictures/Saved Pictures/Computer vision/IMG-20230314-WA0001.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
alpha = 1.5
sharpened_image = sharpen_image_high_boost(gray_image, alpha)

cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
