import numpy as np
import cv2
import imutils
#Podstawowe przesunięcie
#a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
#b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy transformacji M oraz cv2.warpAffine.
#c. Wyświetl wynik.
image = cv2.imread("img.jpg")
cv2.imshow("Orginal", image)
cv2.waitKey(0)
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
#Przesunięcie w przeciwnym kierunku
#a. Wykorzystaj ten sam obraz co wcześniej.
#b. Przesuń go o 20 pikseli w lewo i 50 pikseli w górę.
#c. Wyświetl wynik.
image = cv2.imread("img.jpg")
M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
#Eksperymentowanie z dużymi wartościami przesunięcia
#a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
#b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres oryginalnego obrazu.
image = cv2.imread("img.jpg")
M = np.float32([[1, 0, 330], [0, 1, 330]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Experimental", shifted)
cv2.waitKey(0)
#4. Wykorzystanie funkcji imutils.translate
#a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą imutils.translate .
#b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine . Czy zauważyłeś różnice?
image = cv2.imread("img.jpg")
shifted = imutils.translate(image, 100, 50)
cv2.imshow("Imutils", shifted)
cv2.waitKey(0)
#5. Dynamiczne przesunięcie na podstawie parametrów użytkownika
#a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i typoprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
#b. Sprawdź, jak działa przesunięcie dla różnych wartości.
cv2.destroyAllWindows()
image = cv2.imread("img.jpg")
print("Podaj ilość przesuniecia pixeli w prawo(liczba dodatnia) lub w lewo(liczba ujemna):")
tx = input() 
print("Podaj ilość przesuniecia pixeli w dół(liczba dodatnia) lub w górę(liczba ujemna):")
ty = input()
M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Output", shifted)
cv2.waitKey(0)
