import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    cropped_image = image[0:300, 0:300]
    cv2.imwrite("cropped_image.jpg", cropped_image)
    print("Obraz został zapisany jako cropped_image.jpg")
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")