import cv2

image_path = r"C:\ue\sztuczna\tenis\tenis3.jpg"
image = cv2.imread(image_path)


(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2) 
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()