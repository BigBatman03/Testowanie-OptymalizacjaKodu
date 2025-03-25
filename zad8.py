import cv2

image_path = r"C:\ue\sztuczna\tenis\tenis3.jpg"
image = cv2.imread(image_path)

cv2.imshow("Original", image)

# Pobranie wymiarów obrazu i środka
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# Obrót po 30 stopni, wykonany trzy razy
M1 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated_30_1 = cv2.warpAffine(image, M1, (w, h))

M2 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated_30_2 = cv2.warpAffine(rotated_30_1, M2, (w, h))

M3 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated_30_3 = cv2.warpAffine(rotated_30_2, M3, (w, h))

# Obrót o 90 stopni jednym ruchem
M4 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated_90 = cv2.warpAffine(image, M4, (w, h))

# Wyświetlenie wyników
cv2.imshow("Rotated by 30 Degrees (Sequential)", rotated_30_3)
cv2.imshow("Rotated by 90 Degrees", rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()
