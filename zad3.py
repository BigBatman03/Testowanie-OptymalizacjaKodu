import cv2
image = cv2.imread(r"C:\codeblocks\random-image.jpg")

(height, width, channels) = image.shape
image[height-1, width-1] = (0, 0, 255)
center_x, center_y = width // 2, height // 2
(b, g, r) = image[center_y, center_x]

print("Pixel at center ({}, {}) - Red: {}, Green: {}, Blue: {}".format(center_x, center_y, r, g, b))