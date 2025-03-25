import cv2
import imutils

image_path = r"C:\ue\sztuczna\tenis\tenis3.jpg"
image = cv2.imread(image_path)

cv2.imshow("Original", image)

# Obrót za pomocą cv2.warpAffine
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warpAffine = cv2.warpAffine(image, M, (w, h))

# Obrót za pomocą imutils.rotate
rotated_imutils = imutils.rotate(image, 60)

# Wyświetlenie obu wyników
cv2.imshow("Rotated with cv2.warpAffine", rotated_warpAffine)
cv2.imshow("Rotated with imutils.rotate", rotated_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()
