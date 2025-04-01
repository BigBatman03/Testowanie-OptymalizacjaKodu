import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    lower_half = image[height // 2:, :]  
    cv2.imshow("Lower Half of the Image", lower_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")