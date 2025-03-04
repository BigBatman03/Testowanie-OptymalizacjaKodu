import cv2

# Wczytanie obrazu z pliku
image = cv2.imread("C:\\ue\\sztuczna\\tenis\\tenis2.jpg")
(h, w, c) = image.shape[:3]
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    
print(f'channels: {c}')
 
