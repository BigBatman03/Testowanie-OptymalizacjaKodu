import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(height, width, channels) = image.shape

part_height = height // 3
part_width = width // 3

middle_part = image[part_height:2*part_height, part_width:2*part_width]

cv2.imshow("Srodkowa czesc", middle_part)
cv2.waitKey(0)
cv2.destroyAllWindows()