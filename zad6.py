import cv2
import imutils

image_path = r"C:\ue\sztuczna\tenis\tenis3.jpg"
image = cv2.imread(image_path)

cv2.imshow("Original", image)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
