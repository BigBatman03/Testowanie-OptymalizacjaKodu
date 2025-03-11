import cv2
import numpy as np

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(gray_image)

print(f"Najjaśniejszy piksel znajduje się na współrzędnych {max_loc} z wartością jasności {max_val}")