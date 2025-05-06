import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image.png"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

plt.figure(figsize=(20, 15))

for idx, kernel_size in enumerate(kernel_sizes):
    # 1. Proste rozmycie (cv2.blur)
    blur_simple = cv2.blur(image, kernel_size)

    # 2. Rozmycie Gaussa (cv2.GaussianBlur)
    blur_gaussian = cv2.GaussianBlur(image, kernel_size, 0)

    # 3. Rozmycie medianowe (cv2.medianBlur)
    blur_median = cv2.medianBlur(image, kernel_size[0])

    # 4. Rozmycie dwustronne (cv2.bilateralFilter)
    blur_bilateral = cv2.bilateralFilter(image, kernel_size[0], 75, 75)

    images = [blur_simple, blur_gaussian, blur_median, blur_bilateral]
    titles = [
        f'Simple Blur {kernel_size}',
        f'Gaussian Blur {kernel_size}',
        f'Median Blur {kernel_size[0]}',
        f'Bilateral Filter {kernel_size[0]}'
    ]

    for i in range(4):
        plt.subplot(len(kernel_sizes), 4, idx * 4 + i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')

plt.tight_layout()
plt.show()

# Komentarze dotyczące analizy:
# i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
# - Wraz ze wzrostem rozmiaru kernela efekt rozmycia staje się bardziej intensywny.
# - Dla dużych kerneli szczegóły obrazu są coraz bardziej tracone, a obraz staje się bardziej rozmyty.

# ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
# - Optymalny rozmiar kernela zależy od rodzaju szumu i obrazu:
#   - Dla prostego rozmycia i rozmycia Gaussa: (5x5) lub (9x9) dobrze redukuje szum, ale większe wartości powodują utratę szczegółów.
#   - Dla rozmycia medianowego: (5x5) skutecznie usuwa szum solny i pieprzowy bez znacznej utraty szczegółów.
#   - Dla rozmycia dwustronnego: Rozmiar kernela (9x9) lub (15x15) zachowuje krawędzie, jednocześnie usuwając szum, ale jest bardziej czasochłonny.