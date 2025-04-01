import cv2

image_path = r"C:\programowanie\twarz_okragla-768x1024.webp"
image = cv2.imread(image_path)

if image is not None:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face_roi = image[y:y+h, x:x+w]
            cv2.imshow("Original Image", image)
            cv2.imshow("Cropped Face", face_roi)
            break 
    else:
        print("Nie znaleziono twarzy na obrazie.")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")