import cv2
import numpy as np

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu. Grubość linii: 2 px.
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.line(canvas, (150, 150), (300, 300), blue, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Rysowanie prostokątów, utwórz czarny obraz o wymiarach 400x400 pikseli i narysuj na nim:
# a. Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
# b. Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.rectangle(canvas, (0, 0), (100, 50), green)
cv2.rectangle(canvas, (300, 350), (397, 397), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
# narysuj na nim:
# a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
# b. Czerwony okrąg o promieniu 60 px w środku obrazu.
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (41,41)
cv2.circle(canvas, (centerX, centerY), 40, blue)
(centerX, centerY) = (150,150)
cv2.circle(canvas, (centerX, centerY), 60, red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#Złożona figura
#a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
#px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
#Wszystko powinno być wycentrowane na obrazie.

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.rectangle(canvas, (100, 100), (200, 200), green)
cv2.circle(canvas, (150, 150), 30, green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#5. Eksperymentowanie z pętlą
#a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
#kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
#poprzedniego i mieć środek w tym samym miejscu.

canvas = np.zeros((300, 300, 3), dtype="uint8")
(cordsX, cordsY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
for r in range(0, 100, 10):
    cv2.rectangle(canvas, (cordsX - r, cordsY - r),(cordsX + r, cordsY + r), white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


canvas = cv2.imread("zdj.jpg")
(centerX, centerY) = (192,161)
for r in range(0,20):
    cv2.circle(canvas, (centerX, centerY), r, red)
(centerX, centerY) = (287,156)
for r in range(0,20):
    cv2.circle(canvas, (centerX, centerY), r, red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)