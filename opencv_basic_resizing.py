import cv2
import numpy as np
import imutils

# Wczytaj obraz
image = cv2.imread("example.jpg")
if image is None:
    print("Błąd: Nie udało się wczytać obrazu 'example.jpg'")
    exit()

cv2.imshow("Oryginalny", image)

# 1. Zmniejszenie obrazu o połowę
# a. Wczytaj obraz i zmniejsz jego szerokość oraz wysokość o 50%.
# b. Wyświetl wynik.
(h, w) = image.shape[:2]
dim_half = (w // 2, h // 2)
resized_half = cv2.resize(image, dim_half, interpolation=cv2.INTER_AREA)
cv2.imshow("Zmniejszony o 50%", resized_half)

# 2. Powiększenie obrazu dwukrotnie
# a. Powiększ obraz 2× zarówno w pionie, jak i w poziomie.
# b. Użyj metody cv2.INTER_LINEAR.
dim_double = (w * 2, h * 2)
resized_double = cv2.resize(image, dim_double, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Powiększony 2x", resized_double)

# 3. Zmiana rozmiaru na konkretną wartość
# a. Zmień rozmiar obrazu na dokładnie 200×300 pikseli.
# b. Użyj cv2.resize().
dim_fixed = (300, 200)  # (szerokość, wysokość)
resized_fixed = cv2.resize(image, dim_fixed, interpolation=cv2.INTER_AREA)
cv2.imshow("200x300 pikseli", resized_fixed)

# 4. Porównanie różnych metod interpolacji
# a. Powiększ obraz 3× przy użyciu różnych metod interpolacji ( INTER_NEAREST , INTER_LINEAR , INTER_CUBIC , INTER_LANCZOS4 ).
# b. Wyświetl i porównaj wyniki.
methods = [
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]
for (name, method) in methods:
    resized_method = cv2.resize(image, (w * 3, h * 3), interpolation=method)
    cv2.imshow("Powiększenie 3x - {}".format(name), resized_method)
    print("[INFO] Wyświetlam metodę: {}".format(name))
    cv2.waitKey(0)

# 5. Automatyczne skalowanie na podstawie szerokości
# a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
# b. Użyj imutils.resize().
resized_width = imutils.resize(image, width=500)
cv2.imshow("Skalowanie do szerokości 500 px", resized_width)

# 6. Automatyczne skalowanie na podstawie wysokości
# a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
# b. Wyświetl wynik.
resized_height = imutils.resize(image, height=400)
cv2.imshow("Skalowanie do wysokości 400 px", resized_height)

# 7. Efekty przy skalowaniu w dół
# a. Zmniejsz obraz 5× przy użyciu INTER_AREA.
# b. Sprawdź, jak zmienia się jakość w porównaniu do innych metod.
dim_down = (w // 5, h // 5)
resized_down = cv2.resize(image, dim_down, interpolation=cv2.INTER_AREA)
cv2.imshow("Zmniejszony 5x INTER_AREA", resized_down)

# 8. Efekty przy skalowaniu w górę
# a. Powiększ obraz 4× używając INTER_CUBIC i INTER_LANCZOS4.
# b. Porównaj ostrość obrazu w obu przypadkach.
dim_up = (w * 4, h * 4)
resized_cubic = cv2.resize(image, dim_up, interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(image, dim_up, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Powiększony 4x INTER_CUBIC", resized_cubic)
cv2.imshow("Powiększony 4x INTER_LANCZOS4", resized_lanczos)

# 9. Dynamiczna zmiana rozmiaru w pętli
# a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co 20%.
# b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem ( cv2.waitKey(500) ).
for scale in np.arange(1.0, 3.2, 0.2):  # 3.2 aby dołączyć około 300%
    resized_dynamic = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Skalowanie dynamiczne: {:.0f}%".format(scale * 100), resized_dynamic)
    cv2.waitKey(500)

# 10. Zmiana rozmiaru i zapis pliku
# a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku resized_output.jpg.
resized_output = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized_output)
cv2.imshow("Zmodyfikowany i zapisany", resized_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
