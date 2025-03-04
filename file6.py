import cv2

# Wczytanie obrazu z pliku
image = cv2.imread(r"C:\ue\sztuczna\tenis\tenis2.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)
    cv2.imshow("Obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()