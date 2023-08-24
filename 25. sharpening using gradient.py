import cv2
import numpy as np

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

image_path = "C:/Users/Acer/Pictures/Saved Pictures/Computer vision/IMG-20230314-WA0002.jpg"
original_image = cv2.imread(image_path)

sharpened_image = sharpen_image(original_image)

# Display the original and sharpened images
cv2.imshow("Original Image", original_image)
cv2.imshow("Sharpened Image", sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

