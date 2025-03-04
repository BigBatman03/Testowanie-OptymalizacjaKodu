import cv2

# Wczytanie obrazu z pliku w skali szarości
image = cv2.imread(r"C:\ue\sztuczna\tenis\tenis2.jpg", cv2.IMREAD_GRAYSCALE)
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Obraz w skali szarości", image) # Tworzy okno i wyświetla obraz
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f'Liczba kanałów: 1') # W skali szarości jest tylko jeden kanał
 
