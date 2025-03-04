import cv2

# Wczytanie obrazu z pliku w skali szarości
image = cv2.imread(r"C:\ue\sztuczna\tenis\tenis2.jpg", cv2.IMREAD_GRAYSCALE)
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    # Zapisanie obrazu jako nowy plik
    cv2.imwrite(r"C:\ue\sztuczna\tenis\tenis2_gray.jpg", image)
    print("Obraz zapisano jako tenis2_gray.jpg")