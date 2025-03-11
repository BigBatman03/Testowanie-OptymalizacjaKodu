import cv2
image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))