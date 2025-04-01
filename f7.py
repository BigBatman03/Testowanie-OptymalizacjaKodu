import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    cell_height = height // 3
    cell_width = width // 3

    for row in range(3):
        for col in range(3):
            start_y = row * cell_height
            end_y = start_y + cell_height
            start_x = col * cell_width
            end_x = start_x + cell_width
            cell = image[start_y:end_y, start_x:end_x]
            cv2.imshow(f"Cell {row+1},{col+1}", cell)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")