import cv2

image = cv2.imread(r"C:\ue\sztuczna\tenis\tenis3.jpg")
cv2.imshow("Original", image)

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Rotated by 30 Degrees (Top-Left Corner)", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()