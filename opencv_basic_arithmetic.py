import cv2
import numpy as np

# 1. Porównanie metod dodawania
# a. Wczytaj obraz i zwiększ jego jasność o 50 przy użyciu zarówno NumPy, jak i OpenCV.
image = cv2.imread("img.jpg")
if image is None:
    print("Nie udało się wczytać obrazu 'img.jpg'")
else:
    # Metoda OpenCV
    M = np.ones(image.shape, dtype="uint8") * 50
    added_cv2 = cv2.add(image, M)
    # Metoda NumPy
    added_numpy = image + 50

    # b. Sprawdź, jak różnią się wyniki.
    cv2.imshow("Oryginalny obraz", image)
    cv2.imshow("Jasniejszy cv2.add", added_cv2)
    cv2.imshow("Jasniejszy NumPy", added_numpy)
    cv2.waitKey(0)

# 2. Symulacja efektu "przepalenia" obrazu
# a. Dodaj do każdego piksela wartość 150, ale używając NumPy.
if image is None:
    print("Nie udało się wczytać obrazu 'img.jpg'")
else:
    burn_numpy = image + 150
    # b. Porównaj wynik z operacją cv2.add().
    M_burn = np.ones(image.shape, dtype="uint8") * 150
    burn_cv2 = cv2.add(image, M_burn)

    cv2.imshow("Przepalenie NumPy", burn_numpy)
    cv2.imshow("Przepalenie cv2.add", burn_cv2)
    cv2.waitKey(0)

# 3. Przyciemnianie obrazu
# a. Zmniejsz jasność obrazu o 80 jednostek.
if image is None:
    print("Nie udało się wczytać obrazu 'img.jpg'")
else:
    dark_numpy = image - 80
    M_dark = np.ones(image.shape, dtype="uint8") * 80
    dark_cv2 = cv2.subtract(image, M_dark)

    # b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.
    cv2.imshow("Przyciemniony NumPy", dark_numpy)
    cv2.imshow("Przyciemniony cv2.subtract", dark_cv2)
    cv2.waitKey(0)

# 4. Tworzenie własnego "filtra Instagram"
# a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego +10.
if image is None:
    print("Nie udało się wczytać obrazu 'img.jpg'")
else:
    filter_img = image.copy()
    B, G, R = cv2.split(filter_img)
    R = cv2.add(R, np.ones(R.shape, dtype="uint8") * 30)
    G = cv2.subtract(G, np.ones(G.shape, dtype="uint8") * 20)
    B = cv2.add(B, np.ones(B.shape, dtype="uint8") * 10)
    filter_img = cv2.merge([B, G, R])

    # b. Sprawdź, jak zmienia się obraz.
    cv2.imshow("Filtr Instagram", filter_img)
    cv2.waitKey(0)

# 5. Zastosowanie arytmetyki do detekcji zmian w obrazach
# a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami.
image1 = cv2.imread("scene1.jpg")
image2 = cv2.imread("scene2.jpg")
if image1 is None or image2 is None:
    print("Nie udało się wczytać obrazów 'scene1.jpg' lub 'scene2.jpg'")
else:
    # b. Oblicz ich różnicę.
    diff = cv2.absdiff(image1, image2)
    # c. Zinterpretuj wynik – jakie zmiany są widoczne?
    cv2.imshow("Obraz 1", image1)
    cv2.imshow("Obraz 2", image2)
    cv2.imshow("Różnica", diff)
    cv2.waitKey(0)

cv2.destroyAllWindows()
