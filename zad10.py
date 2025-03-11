import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[100, 100]

diff_r = abs(r1 - r2)
diff_g = abs(g1 - g2)
diff_b = abs(b1 - b2)

print(f"Różnica w wartościach pikseli:")
print(f"R: {diff_r}")
print(f"G: {diff_g}")
print(f"B: {diff_b}")