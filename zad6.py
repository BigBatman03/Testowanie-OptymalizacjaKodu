import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(height, width, channels) = image.shape
center_x, center_y = width // 2, height // 2

top_left_x = center_x - 50
top_left_y = center_y - 50
bottom_right_x = center_x + 50
bottom_right_y = center_y + 50

image[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = (0, 0, 255)

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()