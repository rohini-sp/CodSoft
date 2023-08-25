import cv2
 
classifier = cv2.CascadeClassifier( cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)
 
while True:
    read_ok, frame = capture.read()
    labels = []
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceCoordinates = classifier.detectMultiScale(gray_img)

    for (x, y, w, h) in faceCoordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
    cv2.imshow('Face Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
 
capture.release()
cv2.destroyAllWindows()