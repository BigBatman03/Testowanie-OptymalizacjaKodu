import cv2
import numpy as np

# 1. Kombinacja różnych kształtów i operacji bitowych
# a. Narysuj trójkąt i porównaj go z okręgiem, wykorzystując różne operacje bitowe (AND , OR , XOR , NOT ).
# canvas
canvas = np.zeros((300, 300), dtype="uint8")

#okrąg
circle = canvas.copy()
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Okrąg", circle)

#trójkąt
triangle = canvas.copy()
pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Trójkąt", triangle)

# Operacje bitowe
bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT (Trójkąt)", bitwiseNot)

cv2.waitKey(0)

# b. Sprawdź, jak zmieniają się wyniki w zależności od pozycji kształtów.

M = np.float32([[1, 0, 50], [0, 1, 50]])
shifted_triangle = cv2.warpAffine(triangle, M, (300, 300))
cv2.imshow("Przesunięty Trójkąt", shifted_triangle)

#Operacje bitowe
shifted_and = cv2.bitwise_and(shifted_triangle, circle)
cv2.imshow("AND - Przesunięty", shifted_and)

shifted_or = cv2.bitwise_or(shifted_triangle, circle)
cv2.imshow("OR - Przesunięty", shifted_or)

shifted_xor = cv2.bitwise_xor(shifted_triangle, circle)
cv2.imshow("XOR - Przesunięty", shifted_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Zastosowanie operacji XOR do wykrywania różnic między obrazami
# a. Wczytaj dwa podobne obrazy z drobnymi różnicami.
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

if img1 is None or img2 is None:
    print("Bład wczytania")
else:
    # b. Użyj cv2.bitwise_xor , aby uwidocznić różnice między nimi.
    diff = cv2.bitwise_xor(img1, img2)
    cv2.imshow("Obraz 1", img1)
    cv2.imshow("Obraz 2", img2)
    cv2.imshow("Różnice (XOR)", diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
