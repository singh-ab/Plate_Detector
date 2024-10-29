import cv2

FRAME_WIDTH = 640
FRAME_HEIGHT = 480
MIN_AREA = 200
COLOR = (255, 0, 255)

# Loading the cascade classifier for number plates
n_plate_cascade = cv2.CascadeClassifier("Resources/haar_russian_plate_number.xml")

# Initializing video capture
cap = cv2.VideoCapture("Resources/anpr.mp4")
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(10, 150)

count = 0

while True:
    success, img = cap.read()
    if not success:
        break

    # Converting image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting number plates
    number_plates = n_plate_cascade.detectMultiScale(img_gray, 1.1, 10)

    for (x, y, w, h) in number_plates:
        area = w * h
        if area > MIN_AREA:
            # Drawing rectangle around the number plate
            cv2.rectangle(img, (x, y), (x + w, y + h), COLOR, 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, COLOR, 2)

            # Extracting region of interest (ROI)
            img_roi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    # Displaying the result
    cv2.imshow("Result", img)

    # Saving the detected number plate when 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"Resources/Scanned/NoPlate_{count}.jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        count += 1