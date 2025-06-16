import cv2
import numpy as np

## 1. Maskowanie obszaru twarzy

# a. Wczytaj zdjęcie osoby
image = cv2.imread("osoba.jpg")
cv2.imshow("Oryginał", image)

# b. Stwórz maskę pozostawiającą twarz osoby (elipsa na środku)
mask = np.zeros(image.shape[:2], dtype="uint8")
center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
axes_length = (image.shape[1] // 6, image.shape[0] // 4)
cv2.ellipse(mask, (center_x, center_y), axes_length, 0, 0, 360, 255, -1)
cv2.imshow("Maska: Twarz", mask)

# c. Zastosuj maskę na obrazie i wyświetl wynik
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Maskowana twarz", masked)
cv2.waitKey(0)

# Odpowiedzi:
# - Najlepiej wyciąć twarz za pomocą elipsy/prostokąta, dopasowując kształt i położenie do zdjęcia.
# - Zamaskowana twarz wyodrębnia tylko wybrany obszar, ignorując resztę obrazu.
cv2.destroyAllWindows()


## 2. Ukrywanie określonego obszaru twarzy

# a. Wczytaj zdjęcie osoby
image = cv2.imread("osoba.jpg")
cv2.imshow("Oryginał", image)

# b. Stwórz maskę zasłaniającą oczy (prostokąt z czarnymi oczami)
mask = np.ones(image.shape, dtype="uint8") * 255
start_x, end_x = image.shape[1] // 4, int(image.shape[1] * 0.75)
start_y, end_y = int(image.shape[0]*0.4), int(image.shape[0]*0.55)
cv2.rectangle(mask, (start_x, start_y), (end_x, end_y), (0,0,0), -1)
cv2.imshow("Maska (czarne oczy)", cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))

# c. Zastosuj maskę na obrazie i wyświetl wynik
masked = cv2.bitwise_and(image, mask)
cv2.imshow("Obraz z zasłoniętymi oczami", masked)
cv2.waitKey(0)

# Odpowiedzi:
# - Stosując prostokątną maskę, można łatwo "ocenzurować" oczy na zdjęciu.
# - Piksele tam, gdzie maska = 0, są ustawiane na czarno.
cv2.destroyAllWindows()


## 3. Wykorzystanie maski do ekstrakcji koloru

# a. Wczytaj kolorowy obraz, np. kwiaty, samochód
image = cv2.imread("kwiaty.jpg")
cv2.imshow("Oryginał", image)

# b. Konwersja do HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# c. Maskowanie: wyodrębnianie czerwieni (przykład)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Maska koloru czerwonego", mask)

# d. Tylko czerwone elementy widoczne
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Obraz — tylko wybrany kolor", result)
cv2.waitKey(0)

# Odpowiedzi:
# - Maskowanie w przestrzeni HSV pozwala na precyzyjne wyodrębnienie kolorów.
# - Zakresy HSV można modyfikować w zależności od potrzeb (inny kolor = inne zakresy).
cv2.destroyAllWindows()