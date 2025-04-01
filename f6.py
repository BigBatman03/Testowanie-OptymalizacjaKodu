import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    cropped_fragment = image[0:100, 0:100]
    target_y = height - 100
    target_x = width - 100
    if target_y >= 0 and target_x >= 0:
        image[target_y:target_y+100, target_x:target_x+100] = cropped_fragment
    cv2.imshow("Modified Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")