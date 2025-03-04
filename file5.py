import cv2

# Wczytanie pierwszego obrazu
image1 = cv2.imread(r"C:\ue\sztuczna\tenis\tenis2.jpg")
# Wczytanie drugiego obrazu
image2 = cv2.imread(r"C:\ue\sztuczna\tenis\tenis3.jpg")

# Sprawdzenie, czy obrazy zostały poprawnie wczytane
if image1 is None or image2 is None:
    print("Błąd: nie można wczytać jednego z obrazów!")
else:
    print("Obrazy wczytano poprawnie.")
    # Wyświetlenie pierwszego obrazu
    cv2.imshow("Obraz 1", image1)
    # Wyświetlenie drugiego obrazu
    cv2.imshow("Obraz 2", image2)
    
    while True:
        # Czekanie na naciśnięcie klawisza
        key = cv2.waitKey(1) & 0xFF
        # Zamknięcie okna "Obraz 1" po naciśnięciu klawisza 'q'
        if key == ord('q'):
            cv2.destroyWindow("Obraz 1")
        # Zamknięcie okna "Obraz 2" po naciśnięciu klawisza 'w'
        elif key == ord('w'):
            cv2.destroyWindow("Obraz 2")
        # Wyjście z pętli po zamknięciu obu okien
        if cv2.getWindowProperty("Obraz 1", cv2.WND_PROP_VISIBLE) < 1 and cv2.getWindowProperty("Obraz 2", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()