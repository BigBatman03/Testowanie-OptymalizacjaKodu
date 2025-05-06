import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image.png"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Proste rozmycie (cv2.blur)
blur_simple = cv2.blur(image, (5, 5))

# 2. Rozmycie Gaussa (cv2.GaussianBlur)
blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# 3. Rozmycie medianowe (cv2.medianBlur)
blur_median = cv2.medianBlur(image, 5)

# 4. Rozmycie dwustronne (cv2.bilateralFilter)
blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

titles = ['Original Image', 'Simple Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [image, blur_simple, blur_gaussian, blur_median, blur_bilateral]

plt.figure(figsize=(15, 10))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# Komentarze dotyczące metod:
# i. Która metoda najlepiej usuwa szum?
# - Rozmycie medianowe (cv2.medianBlur) najlepiej usuwa szum solny i pieprz, ponieważ zastępuje każdy piksel medianą sąsiednich pikseli.

# ii. Która metoda zachowuje najwięcej szczegółów?
# - Rozmycie dwustronne (cv2.bilateralFilter) zachowuje najwięcej szczegółów, ponieważ rozmywa obraz, jednocześnie zachowując krawędzie.

# iii. Jakie są zalety i wady każdej metody?
# - Proste rozmycie (cv2.blur):
#   Zalety: Szybkie i proste w implementacji.
#   Wady: Rozmywa zarówno szum, jak i szczegóły, co prowadzi do utraty krawędzi.
# - Rozmycie Gaussa (cv2.GaussianBlur):
#   Zalety: Lepsze niż proste rozmycie w usuwaniu szumu, bardziej naturalne efekty.
#   Wady: Nadal powoduje utratę krawędzi.
# - Rozmycie medianowe (cv2.medianBlur):
#   Zalety: Bardzo skuteczne w usuwaniu szumu solnego i pieprzowego.
#   Wady: Może być wolniejsze dla dużych obrazów i dużych rozmiarów kernela.
# - Rozmycie dwustronne (cv2.bilateralFilter):
#   Zalety: Zachowuje krawędzie, jednocześnie usuwając szum.
#   Wady: Wolniejsze w porównaniu do innych metod, szczególnie dla dużych obrazów.