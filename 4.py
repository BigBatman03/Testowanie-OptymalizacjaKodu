import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image_with_text.png" 
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Zastosowanie różnych metod rozmycia z różnymi parametrami
# 1. Proste rozmycie (cv2.blur)
blur_simple_1 = cv2.blur(image, (3, 3))
blur_simple_2 = cv2.blur(image, (5, 5))
blur_simple_3 = cv2.blur(image, (9, 9))

# 2. Rozmycie Gaussa (cv2.GaussianBlur)
blur_gaussian_1 = cv2.GaussianBlur(image, (3, 3), 0)
blur_gaussian_2 = cv2.GaussianBlur(image, (5, 5), 0)
blur_gaussian_3 = cv2.GaussianBlur(image, (9, 9), 0)

# 3. Rozmycie medianowe (cv2.medianBlur)
blur_median_1 = cv2.medianBlur(image, 3)
blur_median_2 = cv2.medianBlur(image, 5)
blur_median_3 = cv2.medianBlur(image, 9)

# 4. Rozmycie dwustronne (cv2.bilateralFilter)
blur_bilateral_1 = cv2.bilateralFilter(image, 9, 75, 75)
blur_bilateral_2 = cv2.bilateralFilter(image, 15, 150, 150)
blur_bilateral_3 = cv2.bilateralFilter(image, 25, 250, 250)

# Wyświetlenie wyników
titles = [
    'Original Image',
    'Simple Blur (3x3)', 'Simple Blur (5x5)', 'Simple Blur (9x9)',
    'Gaussian Blur (3x3)', 'Gaussian Blur (5x5)', 'Gaussian Blur (9x9)',
    'Median Blur (3)', 'Median Blur (5)', 'Median Blur (9)',
    'Bilateral Filter (9, 75, 75)', 'Bilateral Filter (15, 150, 150)', 'Bilateral Filter (25, 250, 250)'
]
images = [
    image,
    blur_simple_1, blur_simple_2, blur_simple_3,
    blur_gaussian_1, blur_gaussian_2, blur_gaussian_3,
    blur_median_1, blur_median_2, blur_median_3,
    blur_bilateral_1, blur_bilateral_2, blur_bilateral_3
]

plt.figure(figsize=(20, 15))
for i in range(len(images)):
    plt.subplot(4, 4, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# Komentarze dotyczące analizy:
# i. Które metody najmocniej rozmywają tekst?
# - Proste rozmycie (cv2.blur) i rozmycie Gaussa (cv2.GaussianBlur) najmocniej rozmywają tekst, szczególnie przy większych rozmiarach kernela (np. (9x9)).
# - Rozmycie medianowe (cv2.medianBlur) również powoduje znaczną utratę czytelności tekstu przy większych wartościach.

# ii. Które pozwalają zachować jego czytelność?
# - Rozmycie dwustronne (cv2.bilateralFilter) najlepiej zachowuje czytelność tekstu, ponieważ skutecznie redukuje szum, jednocześnie zachowując krawędzie.
# - Parametry (9, 75, 75) lub (15, 150, 150) dają najlepsze rezultaty w zachowaniu czytelności tekstu.