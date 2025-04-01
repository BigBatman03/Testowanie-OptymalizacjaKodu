import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    cropped_region = image[:, width // 2:]
    
    flipped_region = cv2.flip(cropped_region, 1)
    
    image[:, width // 2:] = flipped_region

    cv2.imshow("Modified Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()