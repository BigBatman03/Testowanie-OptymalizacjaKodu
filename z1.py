import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    flipped_image = cv2.flip(image, 1)
    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Image", flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()