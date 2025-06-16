import cv2
import numpy as np

## 1. Wyświetlenie pojedynczych kanałów na obrazie

# a. Wczytaj dowolny obraz
image = cv2.imread("dowolny.jpg")
cv2.imshow("Oryginał", image)

# b. Rozdziel kanały B, G, R i wyświetl je osobno
B, G, R = cv2.split(image)
cv2.imshow("Kanał niebieski (B)", B)
cv2.imshow("Kanał zielony (G)", G)
cv2.imshow("Kanał czerwony (R)", R)

# c. Zapisz te kanały jako osobne obrazy
cv2.imwrite("kanal_B.jpg", B)
cv2.imwrite("kanal_G.jpg", G)
cv2.imwrite("kanal_R.jpg", R)
cv2.waitKey(0)

# Odpowiedzi:
# - Każdy z kanałów to obraz w odcieniach szarości reprezentujący odpowiednią składową barwną.
cv2.destroyAllWindows()


## 2. Analiza cech uwidaczniających się w poszczególnych kanałach

# a. Wybierz obraz z obiektami o różnych kolorach
image = cv2.imread("kolorowe_obiekty.jpg")
cv2.imshow("Oryginał", image)

# b. Rozdziel na kanały
B, G, R = cv2.split(image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)

# c. Poszukaj obiektu, który wyraźnie widać tylko na jednym kanale
# (np. czerwony kwiat będzie jasny tylko na kanale R, niebieski obiekt tylko na kanale B)
cv2.waitKey(0)

# Odpowiedzi:
# - Niebieskie obiekty są jasne tylko na kanale B, czerwone – na R, zielone na G.
# - Ułatwia to detekcję określonych kolorów i analizę obrazu.
cv2.destroyAllWindows()


## 3. Rekonstrukcja obrazu po manipulacji kanałami

# a. Zamień miejscami kanały, np. R, B, G
image = cv2.imread("dowolny.jpg")
B, G, R = cv2.split(image)
img_rbg = cv2.merge([R, B, G])
cv2.imshow("Obraz R, B, G", img_rbg)

# b. Ustaw jeden z kanałów na zero (np. zielony)
G_zero = np.zeros_like(G)
img_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("Obraz bez zielonego", img_no_green)
cv2.waitKey(0)

# Odpowiedzi:
# - Zamiana kanałów radykalnie zmienia kolory.
# - Usunięcie kanału (zerowanie) sprawia, że odpowiednia barwa znika z obrazu.
cv2.destroyAllWindows()


## 4. Wzmocnienie jednego z kanałów

# a. Zwiększ intensywność kanału czerwonego
image = cv2.imread("dowolny.jpg")
B, G, R = cv2.split(image)
R_boosted = cv2.add(R, 50)
img_boosted = cv2.merge([B, G, R_boosted])
cv2.imshow("Wzmocniony czerwony", img_boosted)
cv2.waitKey(0)

# Odpowiedzi:
# - Wzmocnienie kanału czerwonego powoduje, że cały obraz staje się “cieplejszy”, barwy wpadają w czerwień.
cv2.destroyAllWindows()


## 5. Zastosowanie maski do selektywnej modyfikacji kanałów

# a. Wczytaj obraz i stwórz maskę na wybrany obiekt, np. czerwony samochód
image = cv2.imread("czerwony_samochod.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 100])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Maska czerwonego obiektu", mask)

# b. Zwiększ czerwony tylko tam, gdzie maska == 255
B, G, R = cv2.split(image)
R_mod = cv2.add(R, 60, dst=None, mask=mask)
result = cv2.merge([B, G, R_mod])
cv2.imshow("Wzmocniony czerwony tylko na aucie", result)
cv2.waitKey(0)

# Odpowiedzi:
# - Dzięki masce wzmacniamy kolor tylko na jednym obiekcie, a reszta pozostaje bez zmian.
cv2.destroyAllWindows()


## 6. Eksperymentowanie z logiem OpenCV

# a. Pobierz i rozdziel kanały logo OpenCV
logo = cv2.imread("opencv_logo.png")
B, G, R = cv2.split(logo)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)

# b. Zamiana niebieskiego z czerwonym
logo_swap = cv2.merge([R, G, B])
cv2.imshow("Logo: zamiana czerwony <-> niebieski", logo_swap)
cv2.waitKey(0)

# c. Usunięcie (wyzerowanie) kanału zielonego
G_zero = np.zeros_like(G)
logo_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("Logo bez zielonego kanału", logo_no_green)
cv2.waitKey(0)

# Odpowiedzi:
# - Logo nabiera zupełnie innych kolorów po przestawieniu kanałów lub wyzerowaniu jednego z nich.
cv2.destroyAllWindows()