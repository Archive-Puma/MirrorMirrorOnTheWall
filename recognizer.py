# Import OpenCV module
import cv2

# Get the camera
camera = cv2.VideoCapture(0)

# Create the classifier
detector = cv2.CascadeClassifier(
    "data/third/haarcascade_frontalface_default.xml")

# Create the recognizer
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load("data/recognizer/trainingData.yml")

ID = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

# Show camera until exit signal
while(True):

    # Capture frame-by-frame
    ret, frame = camera.read()

    # Convert camera frame to grayscale
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Focus on the faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        ID, conf = recognizer.predict(gray[y:y + h, x:x + h])

        if(ID == 2):
            ID = "ACACIA"
        elif (ID == 1):
            ID = "ERMUNDO"

        cv2.cv.PutText(cv2.cv.fromarray(frame), str(ID), (x, y + h), font, 255)

    # Display the modified frame
    cv2.imshow('Mirror, Mirror on the Wall...', frame)

    # Exit when press 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the camera
camera.release()
cv2.destroyAllWindows()
