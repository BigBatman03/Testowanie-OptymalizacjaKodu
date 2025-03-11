import cv2
image = cv2.imread(r"C:\codeblocks\random-image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

image[100, :] = (0, 255, 0)

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()