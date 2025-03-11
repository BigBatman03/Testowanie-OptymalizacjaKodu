import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(height, width, channels) = image.shape
mid_x, mid_y = width // 2, height // 2
image[0:mid_y, 0:mid_x] = (255, 0, 0)

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()