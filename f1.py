import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    roi = image[0:100, 0:100]  
    cv2.imshow("Original Image", image)
    cv2.imshow("ROI (100x100 from top-left corner)", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")