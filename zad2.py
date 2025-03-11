import cv2
image = cv2.imread(r"C:\codeblocks\random-image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

(height, width, channels) = image.shape
image[height-1, width-1] = (0, 0, 255)

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()