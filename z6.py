import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    print("Wybierz sposób odbicia:")
    print("0 - Pionowe")
    print("1 - Poziome")
    print("-1 - Oba")
    
    try:
        flip_code = int(input("Podaj kod odbicia (0, 1, -1): "))
        if flip_code in [0, 1, -1]:
            flipped_image = cv2.flip(image, flip_code)
            cv2.imshow("Original Image", image)
            cv2.imshow("Flipped Image", flipped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Nieprawidłowy kod odbicia. Wybierz 0, 1 lub -1.")
    except ValueError:
        print("Podano nieprawidłową wartość. Wprowadź liczbę całkowitą.")
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")