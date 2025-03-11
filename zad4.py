import cv2

image = cv2.imread(r"C:\codeblocks\random-image.jpg")
(height, width, channels) = image.shape

x = int(input("Podaj wspolrzedne x: "))
y = int(input("Podaj wspolrzedne y: "))

if 0 <= x < width and 0 <= y < height:
    image[y, x] = (0, 0, 0)
    print(f"Pixel na ({x}, {y}) zostal zmieniony na czarny")
else:
    print("Wspolrzedne wykraczaja poza obraz.")

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()