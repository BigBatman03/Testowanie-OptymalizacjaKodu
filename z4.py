import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both_axes = cv2.flip(image, -1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Horizontally Flipped Image", flipped_horizontal)
    cv2.imshow("Vertically Flipped Image", flipped_vertical)
    cv2.imshow("Flipped Image (Both Axes)", flipped_both_axes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()