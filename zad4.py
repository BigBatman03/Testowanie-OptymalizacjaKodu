import cv2

image = cv2.imread(r"C:\ue\sztuczna\tenis\tenis3.jpg")
cv2.imshow("Original", image)

angle = float(input("Podaj kąt obrotu: "))

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow(f"Rotated by {angle} Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()