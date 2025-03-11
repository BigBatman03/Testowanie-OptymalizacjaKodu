import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
cv2.imshow("Oryginalny obraz", image)
cv2.waitKey(0)

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()