import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image.png" 
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rozmycie dwustronne z różnymi wartościami parametrów
bilateral_1 = cv2.bilateralFilter(image, 9, 75, 75)  # Domyślne parametry
bilateral_2 = cv2.bilateralFilter(image, 15, 150, 150)  # Większe parametry
bilateral_3 = cv2.bilateralFilter(image, 25, 250, 250)  # Jeszcze większe parametry

# Porównanie z innymi metodami rozmycia
blur_simple = cv2.blur(image, (9, 9))  # Proste rozmycie
blur_gaussian = cv2.GaussianBlur(image, (9, 9), 0)  # Rozmycie Gaussa
blur_median = cv2.medianBlur(image, 9)  # Rozmycie medianowe

titles = [
    'Original Image', 
    'Bilateral Filter (9, 75, 75)', 
    'Bilateral Filter (15, 150, 150)', 
    'Bilateral Filter (25, 250, 250)', 
    'Simple Blur (9x9)', 
    'Gaussian Blur (9x9)', 
    'Median Blur (9)'
]
images = [image, bilateral_1, bilateral_2, bilateral_3, blur_simple, blur_gaussian, blur_median]

plt.figure(figsize=(20, 15))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# Komentarze dotyczące analizy:
# i. Czy rozmycie dwustronne skutecznie redukuje szum?
# - Tak, rozmycie dwustronne skutecznie redukuje szum, szczególnie dla wyższych wartości parametrów (np. (15, 150, 150) lub (25, 250, 250)).

# ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
# - Tak, rozmycie dwustronne zachowuje krawędzie znacznie lepiej niż proste rozmycie, rozmycie Gaussa i rozmycie medianowe. Jest to jego główna zaleta.

# iii. Jakie wartości parametrów dają najlepsze rezultaty?
# - Optymalne wartości parametrów zależą od obrazu:
#   - Dla obrazów z umiarkowanym szumem: (9, 75, 75) daje dobre rezultaty.
#   - Dla obrazów z większym szumem: (15, 150, 150) lub (25, 250, 250) skutecznie redukuje szum, ale może być bardziej czasochłonne.