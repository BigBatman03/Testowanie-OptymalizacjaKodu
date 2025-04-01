import cv2

image_path = "C:\\ue\\sztuczna\\tenis\\tenis2.jpg"
image = cv2.imread(image_path)

if image is not None:
    height, width, _ = image.shape
    roi_width = 100
    start_x = 0

    while True:
        end_x = start_x + roi_width
        if end_x > width:
            break

        roi = image[:, start_x:end_x]
        cv2.imshow("Sliding ROI", roi)

        key = cv2.waitKey(0)
        if key == 27: 
            break

        start_x += 10

    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")