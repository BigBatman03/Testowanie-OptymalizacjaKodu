import cv2

image_path = r"C:\ue\sztuczna\tenis\tenis3.jpg"
image = cv2.imread(image_path)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

for angle in range(0, 361, 15):
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    cv2.imshow(f"Rotated by {angle} Degrees", rotated)
    
    cv2.waitKey(500)

cv2.destroyAllWindows()
