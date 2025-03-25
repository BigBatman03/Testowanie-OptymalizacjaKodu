import imutils
import cv2

image = cv2.imread()

cv2.imshow("Original", image)

rotated = imutils.rotate(image, 180)

cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
