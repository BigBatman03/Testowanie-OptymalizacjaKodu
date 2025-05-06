import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image.png"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

noise_gaussian = image.copy()
cv2.randn(noise_gaussian, (0, 0, 0), (50, 50, 50))
image_with_gaussian_noise = cv2.add(image, noise_gaussian)

noise_salt_pepper = image.copy()
prob = 0.02
for i in range(noise_salt_pepper.shape[0]):
    for j in range(noise_salt_pepper.shape[1]):
        rand = np.random.rand()
        if rand < prob:
            noise_salt_pepper[i, j] = [0, 0, 0]
        elif rand > 1 - prob:
            noise_salt_pepper[i, j] = [255, 255, 255]

# Zastosowanie różnych metod rozmycia
# 1. Proste rozmycie (cv2.blur)
blur_simple = cv2.blur(image_with_gaussian_noise, (5, 5))

# 2. Rozmycie Gaussa (cv2.GaussianBlur)
blur_gaussian = cv2.GaussianBlur(image_with_gaussian_noise, (5, 5), 0)

# 3. Rozmycie medianowe (cv2.medianBlur)
blur_median = cv2.medianBlur(noise_salt_pepper, 5)

# 4. Rozmycie dwustronne (cv2.bilateralFilter)
blur_bilateral = cv2.bilateralFilter(image_with_gaussian_noise, 9, 75, 75)

# Wyświetlenie wyników
titles = [
    'Original Image', 
    'Gaussian Noise', 
    'Salt & Pepper Noise', 
    'Simple Blur', 
    'Gaussian Blur', 
    'Median Blur', 
    'Bilateral Filter'
]
images = [
    image, 
    image_with_gaussian_noise, 
    noise_salt_pepper, 
    blur_simple, 
    blur_gaussian, 
    blur_median, 
    blur_bilateral
]

plt.figure(figsize=(20, 15))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# Komentarze dotyczące analizy:
# - Rozmycie medianowe (cv2.medianBlur) najlepiej usuwa szum soli i pieprzu, ponieważ zastępuje każdy piksel medianą sąsiednich pikseli.
# - Rozmycie Gaussa (cv2.GaussianBlur) i rozmycie dwustronne (cv2.bilateralFilter) są skuteczne w redukcji szumu Gaussa, ale rozmycie dwustronne lepiej zachowuje krawędzie.
# - Proste rozmycie (cv2.blur) usuwa szum, ale powoduje utratę szczegółów i rozmycie krawędzi.