import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "image_with_objects.png" 
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.circle(mask, (250, 250), 100, 255, -1) 

blurred_background = cv2.GaussianBlur(image, (21, 21), 0)

foreground = cv2.bitwise_and(image, image, mask=mask) 
background = cv2.bitwise_and(blurred_background, blurred_background, mask=cv2.bitwise_not(mask))  # Wyodrębnienie tła
result = cv2.add(foreground, background) 

# Wyświetlenie wyników
titles = ['Original Image', 'Mask', 'Blurred Background', 'Result']
images = [image, mask, blurred_background, result]

plt.figure(figsize=(20, 10))
for i in range(len(images)):
    plt.subplot(1, 4, i + 1)
    if i == 1:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

# Komentarze dotyczące analizy:
# - Efekt głębi ostrości został osiągnięty poprzez rozmycie tła za pomocą cv2.GaussianBlur.
# - Główny obiekt został wyodrębniony za pomocą maski i pozostawiony wyraźny.
# - Maska może być przygotowana ręcznie lub automatycznie (np. za pomocą segmentacji obrazu).