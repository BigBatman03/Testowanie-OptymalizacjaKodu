import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    print(f"Rozmiar obrazu: szerokość={width}, wysokość={height}")
    
    try:
        startX = int(input("Podaj startX (0 - szerokość obrazu): "))
        endX = int(input("Podaj endX (startX - szerokość obrazu): "))
        startY = int(input("Podaj startY (0 - wysokość obrazu): "))
        endY = int(input("Podaj endY (startY - wysokość obrazu): "))
        
        if 0 <= startX < endX <= width and 0 <= startY < endY <= height:
            roi = image[startY:endY, startX:endX]
            cv2.imshow("Original Image", image)
            cv2.imshow("Selected ROI", roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Podane wartości są nieprawidłowe. Upewnij się, że mieszczą się w zakresie obrazu.")
    except ValueError:
        print("Podano nieprawidłowe wartości. Wprowadź liczby całkowite.")
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")