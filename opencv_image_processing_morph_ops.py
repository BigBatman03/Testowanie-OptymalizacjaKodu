import cv2
import numpy as np

## 1. Analiza wpływu erozji na obrazy

# a. Wczytaj obraz binarny zawierający różne kształty
image = cv2.imread('ksztalty_binarny.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Oryginał", image)

# b. Zastosuj operację erozji z różnymi elementami strukturalnymi
kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

eroded_square = cv2.erode(image, kernel_square, iterations=1)
eroded_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)
cv2.imshow("Erozja - kwadrat 5x5", eroded_square)
cv2.imshow("Erozja - elipsa 5x5", eroded_ellipse)
cv2.waitKey(0)

# c. Opis zmian:
# - Po erozji obiekty stają się cieńsze, mogą znikać cienkie fragmenty.
# - Kwadratowy kernel silniej "obcina" narożniki niż eliptyczny.

cv2.destroyAllWindows()


## 2. Eksperymentowanie z dylatacją

# a. Pobierz obraz z cienkimi liniami/przerwami
image = cv2.imread('linia_i_przerwy.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Oryginalny obraz", image)

# b. Zastosuj dylatację z różną liczbą iteracji
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
for i in range(1, 5):
    dilated = cv2.dilate(image, kernel, iterations=i)
    cv2.imshow(f"Dylatacja: {i} iteracji", dilated)
    cv2.imwrite(f"dylated_{i}.png", dilated)
    cv2.waitKey(0)

# c. Tabela:
# | Iteracje | Grubość linii |
# |----------|---------------|
# |     1    |    ...        |
# |     2    |    ...        |
# |     3    |    ...        |
# |     4    |    ...        |

# Im więcej iteracji, tym linie są grubsze i szybciej znikają przerwy.
cv2.destroyAllWindows()


## 3. Usuwanie szumu za pomocą otwarcia

# a. Wczytaj obraz z szumem typu sól i pieprz
image = cv2.imread('szum_sp.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Oryginał - szum", image)

# b. Zastosuj otwarcie z różnymi rozmiarami elementu
for ks in [(3,3), (5,5), (7,7)]:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ks)
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Otwieranie kernel={ks}", opened)
    cv2.waitKey(0)

# c. Skuteczność:
# - Lepsze usuwanie szumu przy większym kernelu, ale możliwa utrata detalu.
cv2.destroyAllWindows()


## 4. Łączenie przerw w obiektach za pomocą zamknięcia

# a. Pobierz obraz z literami/przerwami
image = cv2.imread('litery_przerwy.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Przed zamknięciem", image)

# b. Wykorzystaj zamknięcie dla różnych kernelów i kształtów
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

closing_rect = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_rect)
closing_ellipse = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_ellipse)
cv2.imshow("Zamknięcie (prostokąt)", closing_rect)
cv2.imshow("Zamknięcie (elipsa)", closing_ellipse)
cv2.waitKey(0)

# c. Efekty:
# - Zamknięcie wypełnia przerwy i łączy fragmenty znaków.
# - Różne kształty kernelów dają nieco inne efekty w szczegółach znaków.
cv2.destroyAllWindows()


## 5. Eksperymentowanie z różnymi elementami strukturalnymi

# a. Wybrany obraz
image = cv2.imread('ksztalty_binarny.png', cv2.IMREAD_GRAYSCALE)

# b. Wszystkie operacje dla różnych kształtów kernelów
kernels = {
    "Kwadrat": cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
    "Krzyż": cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)),
    "Elipsa": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
}

for name, kernel in kernels.items():
    erosion = cv2.erode(image, kernel, iterations=1)
    dilation = cv2.dilate(image, kernel, iterations=1)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f"Erozja - {name}", erosion)
    cv2.imshow(f"Dylatacja - {name}", dilation)
    cv2.imshow(f"Otwarcie - {name}", opening)
    cv2.imshow(f"Zamknięcie - {name}", closing)
    cv2.imshow(f"Gradient - {name}", gradient)
    cv2.waitKey(0)

# c. Porównanie:
# - Kwadratowy: silnie zmienia kształty, mocno "ścina" kąty.
# - Elipsa: łagodniejsze obróbki.
# - Krzyż: ciekawe efekty przy drobnych strukturach.
cv2.destroyAllWindows()


## 6. Przygotowanie własnego przykładu zastosowania operacji morfologicznych

# a. Przykład: poprawa czytelności tablicy rejestracyjnej na zdjęciu
image = cv2.imread('tablica_rej.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Próg do uzyskania obrazu binarnego
_, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("Oryginał binarny", binary)

# b. Operacje morfologiczne
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Po otwarciu", opened)
cv2.imshow("Po zamknięciu", closed)
cv2.waitKey(0)

# - Efekt: usunięto szum z tła i domknięto cyfry/tablice, poprawiając czytelność.
cv2.destroyAllWindows()